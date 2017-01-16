using Gtk;
using Cairo;

// http://stackoverflow.com/questions/8371779/how-to-take-screenshot-in-vala

int main (string[] args) {
    Gtk.init (ref args);

    int  width, height;

    Gdk.Window win = Gdk.get_default_root_window();

    width = win.get_width();
    height = win.get_height();

    Gdk.Pixbuf screenshot = Gdk.pixbuf_get_from_window(win, 0, 0, width, height);

    screenshot.save("screenshot.png","png");
    return 0;
}

//  valac --pkg gtk+-3.0 --pkg gdk-3.0  screenshot.vala 
