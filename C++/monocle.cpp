#include "magArea.h"
#include <gtkmm.h>
#include <gtkmm/application.h>
#include <thread>
#include <iostream>
#include <X11/Xlib.h>
#include <cairomm/context.h>
#include <gdk-pixbuf/gdk-pixbuf.h>

void mousepos(Gtk::Window *win);
int key_event(GtkWidget *widget, GdkEventKey *event);

using namespace std;

Display *disp = XOpenDisplay(0);
Window root, child;
int X, Y, rootX, rootY, winX, winY;
unsigned int mask;

int width = 400; int height = 300;

/*******************************************/

int main(int argc, char *argv[]) {
	auto app =
		Gtk::Application::create(argc, argv,
			"org.gtkmm.examples.base");

	Gtk::Window window;
	window.set_size_request(width, height);
	window.property_resizable() = false;
	window.set_opacity(0.7);
	window.set_icon_from_file("mag.png");

	magArea area;
	window.add(area);

	//run mousepos concurrently
	thread t1(mousepos, &window);
	t1.detach();
	window.show_all();

	return app->run(window);
}

void mousepos(Gtk::Window *win) {
	while(true) {
        //get the current mouse coordinates
		bool onScreen = XQueryPointer(disp, DefaultRootWindow(disp),
			&root, &child, &rootX, &rootY, &winX, &winY, &mask);

		if (onScreen) {
			X = rootX - width/2;
			Y = rootY - height/2;

			win->move(X,Y);
		}

		this_thread::sleep_for (chrono::milliseconds(10));

	}
}

int key_event(GtkWidget *widget, GdkEventKey *event) {
    return 0;
}

void getScreen() {
     XImage *image = XGetImage(disp,root, 0,0 , width,height,AllPlanes, ZPixmap);
}
