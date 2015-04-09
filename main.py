import os
import pango
import sys
import subprocess
import threading

try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)

def draw_pixbuf(widget, event):
        print("test")
        path = "./ApachenatorBackground.png"
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        scaled_buf = pixbuf.scale_simple(869,440,gtk.gdk.INTERP_BILINEAR)
        widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], scaled_buf, 0, 0, 0,0)

class Application():
    def __init__(self):
        #Set the Glade file
        self.gladefile = "UI.glade"  
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.main_window = self.builder.get_object("Main Window") 
        self.fixed1 = self.builder.get_object("fixed1") 
        self.running = False
        self.fixed1.connect('expose-event', draw_pixbuf)

        self.button = self.builder.get_object("button1")
        label = self.button.child
        label.modify_font(pango.FontDescription("eufm10 Bold 26"))
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))

        self.button = self.builder.get_object("button2")
        label = self.button.child
        label.modify_font(pango.FontDescription("eufm10 Bold 26"))
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))

        self.button = self.builder.get_object("button3")
        label = self.button.child
        label.modify_font(pango.FontDescription("eufm10 Bold 26"))
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))

        self.button = self.builder.get_object("Connect")
        label = self.button.child
        label.modify_font(pango.FontDescription("eufm10 Bold 26"))
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))

        self.status = self.builder.get_object("Status")
        self.status.modify_font(pango.FontDescription("eufm10 Bold 26"))
        self.status.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))

        self.main_window.show_all()

    def connectHandler(self,x):
        if(self.running):
            thread = threading.Thread(target=lambda: subprocess.call(['x-www-browser','localhost']))
            thread.start()

    def startHandler(self,x):
        if not self.running:
            thread = threading.Thread(target= lambda: subprocess.call(['gksudo','apachectl','start']))
            thread.start()
            self.running = True

    def restartHandler(self,x):
        thread = threading.Thread(target=lambda: subprocess.call(['gksudo','apachectl','restart']))
        thread.start()
        self.running = True

    def stopHandler(self,x):
        thread = threading.Thread(target=lambda: subprocess.call(['gksudo','apachectl','stop']))
        thread.start()
        self.running = False

def main():
    # Initalize and run the application
    applicaton = Application()
    gtk.main()

if __name__ == "__main__":
    main()

