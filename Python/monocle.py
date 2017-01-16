#!/usr/bin/env python
# 
# Note: you'll need python-xlib, python-gtk2, and cairo

# http://lethalman.blogspot.com/2009/04/create-cairo-surface-from-pixbuf.html

import sys
import os

from time import sleep

import gtk
gtk.gdk.threads_init()

import threading

from Xlib import display
import cairo


old_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')

width = 250
height = 200

def mousepos():
    """mousepos() --> [x, y] the current mouse coordinates (Xlib)"""
    data = display.Display().screen().root.query_pointer()._data
    return [data["root_x"], data["root_y"]]


class MouseThread(threading.Thread):
    def __init__(self, parent, label, window):
        threading.Thread.__init__(self)
        self.label = label
        self.window = window
        self.killed = False

    def run(self):
        try:
            while True:
                if self.stopped():
                    break
                text = "{0}".format(mousepos())
                self.label.set_text(text)
                xcenter = mousepos()[0]-width/2
                ycenter = mousepos()[1]-height/2
                # make the magnifier follow the mouse
                self.window.move(xcenter, ycenter)
                self.window.show()
                sleep(0.007)
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

    def kill(self):
        self.killed = True

    def stopped(self):
        return self.killed
        

class Magnifier(gtk.Window):

	def __init__(self):
		super(Magnifier, self).__init__()
		self.set_icon_from_file("mag.png")
		
		# This is the actual magnification area window
		self.set_size_request(width, height)
		self.set_resizable(False)
		self.connect("destroy", self.quit)
		self.connect("key-press-event", self.quit)
		
		label = gtk.Label()
		
		screen = self.get_screen()
		colormap = screen.get_rgba_colormap()
		if colormap != None and screen.is_composited():
			self.set_colormap(colormap)
		
		self.colormap = colormap
		self.set_app_paintable(True)
		# self.connect("expose-event", self.draw_transparency)
		self.connect("expose-event", self.draw_magnify)
		
		
		self.mouseThread = MouseThread(self, label, self)
		self.mouseThread.start()
		
		# put the mosue coordinates on the window
		fixed = gtk.Fixed()
		fixed.put(label, 10, 10)
		
		self.add(fixed)
		self.show_all()
		
	def draw_transparency(self, widget, event):
		cr = widget.get_window().cairo_create()
		cr.set_source_rgba(.2,.2,.2,0.3)
		cr.set_operator(cairo.OPERATOR_SOURCE)
		cr.paint()
		cr.set_operator(cairo.OPERATOR_OVER)
		return False
		
	def draw_magnify(self, widget, event):
		cr = widget.get_window().cairo_create()
		
		root_win = Gdk.get_default_root_window()
		pb = Gdk.pixbuf_get_from_window(root_win, 0, 0, width, height)
		
		self.img = cairo.ImageSurface.create_from_png("mag.png")
		cr.set_source_surface(self.img0, 10, 10)
		cr.paint()
		
	def quit(self, widget):
		self.mouseThread.kill()
		gtk.main_quit()
		
if __name__ == '__main__':
    app = Magnifier()
    gtk.main()
