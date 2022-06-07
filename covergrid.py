#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.set_border_width(10)


        grid = Gtk.Grid()

        image1 = Gtk.Image()
        image1.set_from_file("index16/cover0001.png")
        grid.attach(image1,1, 1, 1, 1)

        image2 = Gtk.Image()
        image2.set_from_file("index16/cover0002.png")
        grid.attach(image2, 2, 1, 1 ,1)

        image3 = Gtk.Image()
        image3.set_from_file("index16/cover0003.png")
        grid.attach(image3, 3, 1, 1, 1)

        image4 = Gtk.Image()
        image4.set_from_file("index16/cover0004.png")
        grid.attach(image4, 4, 1, 1, 1)

        image5 = Gtk.Image()
        image5.set_from_file("index16/cover0005.png")
        grid.attach(image5, 1, 2, 1, 1)

        image6 = Gtk.Image()
        image6.set_from_file("index16/cover0006.png")
        grid.attach(image6, 2, 2, 1, 1,)

        image7 = Gtk.Image()
        image7.set_from_file("index16/cover0007.png")
        grid.attach(image7, 3, 2, 1, 1)

        image8 = Gtk.Image()
        image8.set_from_file("index16/cover0008.png")
        grid.attach(image8, 4, 2, 1, 1)

        image9 = Gtk.Image()
        image9.set_from_file("index16/cover0009.png")
        grid.attach(image9, 1, 3, 1, 1)

        image10 = Gtk.Image()
        image10.set_from_file("index16/cover0010.png")
        grid.attach(image10, 2, 3, 1, 1)

        image11 = Gtk.Image()
        image11.set_from_file("index16/cover0011.png")
        grid.attach(image11, 3, 3, 1, 1)

        image12 = Gtk.Image()
        image12.set_from_file("index16/cover0012.png")
        grid.attach(image12, 4, 3, 1, 1)

        image13 = Gtk.Image()
        image13.set_from_file("index16/cover0013.png")
        grid.attach(image13, 1, 4, 1, 1)

        image14 = Gtk.Image()
        image14.set_from_file("index16/cover0014.png")
        grid.attach(image14, 2, 4, 1, 1)

        image15 = Gtk.Image()
        image15.set_from_file("index16/cover0015.png")
        grid.attach(image15, 3, 4, 1, 1)

        image16 = Gtk.Image()
        image16.set_from_file("index16/cover0016.png")
        grid.attach(image16, 4, 4, 1, 1)

        self.add(grid)
        self.set_title("CoverGrid")
        self.connect("destroy", Gtk.main_quit)


win = MyWindow()
win.show_all()
Gtk.main()
