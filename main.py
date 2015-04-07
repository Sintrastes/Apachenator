import os

import sys
import subprocess
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

os.system("apache")

class Application():
    """This is an Hello World GTK application"""
    def __init__(self):
        #Set the Glade file
        self.gladefile = "UI.glade"  
        

        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.main_window = self.builder.get_object("Main Window") 


        self.main_window.show_all()

    def connectHandler(self,x):
        pass

    def startHandler(self,x):
        subprocess.call(['sudo','apachectl','start'])

    def restartHandler(self,x):
        subprocess.call(['sudo','apachectl','restart'])

    def stopHandler(self,x):
        subprocess.call(['sudo','apachectl','stop'])

def main():
    # Initalize and run the application
    applicaton = Application()
    gtk.main()

if __name__ == "__main__":
    main()

