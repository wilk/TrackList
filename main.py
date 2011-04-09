#! /usr/bin/env python

#import main_window as mw
#import listing as l

import gtk
import view
import model
import controller

if __name__ == "__main__":
#	mainWin = mw.MainWindow()
#	mainWin.fileList.connect (l.createList)
	m = model.MainModel ()
	v = view.MainWindowView ()
	c = controller.MainController (m, v)
	gtk.main ()
