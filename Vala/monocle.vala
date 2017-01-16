using Gtk;
using Cairo;
using X; // x11

// http://stackoverflow.com/questions/8371779/how-to-take-screenshot-in-vala
// https://mail.gnome.org/archives/vala-list/2012-January/msg00079.html
// https://valadoc.org/x11/X.Display.html

class MainWindow : Gtk.Window {

    public static int main (string[] args) {
        Gtk.init(ref args);
        
    ////////// This is where the magic happens /////////
        int width, height;
        Gdk.Window root_win = Gdk.get_default_root_window();
        width = root_win.get_width();
        height = root_win.get_height();
        
        Gdk.Pixbuf screenshot = Gdk.pixbuf_get_from_window(root_win, 0, 0, width, height);
    /////////////////////////////////////////////////////
        
        //X.Window disp = X.Display.default_root_window();
        
        //var display = Gdk.x11_get_default_xdisplay ();
        
        
        
        var window = new MainWindow();
        window.destroy.connect(Gtk.main_quit);
        window.show_all();
        
        Gtk.main();
        return 0;
    }
    
    public MainWindow() {
        
        // set the application icon
        try {
            this.icon = new Gdk.Pixbuf.from_file("mag.png");
        } catch (Error e) {
            stderr.printf("Could not load application icon: %s\n", e.message);
        }
        
        this.set_default_size(250, 200);
        this.set_resizable(false);
        this.destroy.connect(Gtk.main_quit);
        
        Gtk.DrawingArea da = new Gtk.DrawingArea();
        this.add(da);
    }

}

class MouseThread {
    
    public MouseThread(Gtk.Window win) {
        // getCoordinates
        // moveWindow, i.e. win.move(X,Y);
        // paintWindow
        // sleep
    }

    public getCoordinates() {
        // X.Window
    }
    
    public paintWindow() {
        //pass
    }
}

//  valac --pkg gtk+-3.0 --pkg gdk-3.0 --pkg x11 monocle.vala 
