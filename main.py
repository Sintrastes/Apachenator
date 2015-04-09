import os

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
        path = "./test.jpeg"
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

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

