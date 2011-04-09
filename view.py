#! /usr/bin/env python

#View
#    Contains a set of widgets, and the methods for manipulating them. The set of widgets can be build out of a GtkBuilder file, or glade file.

from gtkmvc import View

class MainWindowView (View):
	""" Main GUI Window Class """
	
	def __init__ (self):
		""" Main GUI constructor """
		View.__init__(self, "main_window.glade", "windowMain")
		self.dirBase = self['dirChooserSong'].get_filename ()
	
	def setSameDir (self, dirSong):
		""" Sets the same filename of the other filechooser (dirChooserList) """
		self['dirChooserList'].set_current_folder (dirSong)
	
	def resetFileChoosers (self):
		""" Reset both filechoosers current folder """
		self['dirChooserSong'].set_current_folder (self.dirBase)
		self['dirChooserList'].set_current_folder (self.dirBase)
	
	pass
