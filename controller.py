#! /usr/bin/env python

#Controller

#    It is a particular kind of Observer, connected to one model and to one or more views. It contains the GUI logic, and all handlers for GUI signals. E.g.

#        * The code that makes a progress bar advance in the view as the music file is played by the model.

#Adapter

#    Adapts the content of one widget (or a set of widgets) into the view with one observable property into the model. An adapter keeps the content of an observable property up-to-dated with the content of a widget, and viceversa. Adapters live into the controllers. E.g.

#        * An adapter that bounds property current_perc with a progress bar widget into the view.


import gtk
from gtkmvc import Controller

class MainController (Controller):
	
	def __init__ (self, model, view):
		Controller.__init__ (self, model, view)
	
#	def register_view (self, view):
#		return
	
	#def register_adapters (self):
	#	return
	
	# ------------------------------------------------------------
	#      GTK Signal handlers
	# ------------------------------------------------------------
	
	def on_windowMain_destroy (self, window):
		gtk.main_quit ()
		return False
	
	def on_menuQuit_activate (self, menu):
		gtk.main_quit ()
		return False
	
	def on_dirChooserSong_current_folder_changed (self, fc):
		if (self.model.checkDir (fc.get_filename ())):
			self.view.setSameDir (fc.get_filename ())
	
	#TODO: check permissions on directory selected with checkDir () method of model, showing an error dialog
#	def on_dirChooserList_current_folder_changed (self, filechooser):
		#
	
	def on_buttonClear_clicked (self, button):
		self.view.resetFileChoosers ()
	
	def on_buttonApply_clicked (self, button):
		if ((self.model.checkDir (self.view['dirChooserSong'].get_filename ())) and (self.model.checkDir (self.view['dirChooserList'].get_filename ()))):
			self.model.createList (self.view['dirChooserSong'].get_filename (), self.view['dirChooserList'].get_filename ())
	
	pass
