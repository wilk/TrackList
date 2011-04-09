#! /usr/bin/env python

#Model

#    Contains the logic of the application, the data that are independent on the GUI. For example, in a music player:

#        * The list of the mp3 file names.
#        * The methods for playing the files in the list.

#Observer
#    It is an entity interested in observing some parts of one or more Models. Observers are used to react to certain changes in models without creating explicit dependencies or links with them.
#Observable Property

#    It is an attribute of the Model, that is supposed to be observable by one or more observers connected to the model. For example:

#        * The property current_perc holding the % of the mp3 file that is being played.

#    Observable properties can be concrete (data is phisically stored in the model), or logical (data is function of other properties, or stored outside the model, like in a database.)


import os
import glob
from gtkmvc import Model

class MainModel (Model):
	
	def checkDir (self, dirSong):
		""" Checks if the dirSong exists and if the user can read and write on it """
		return (os.path.exists (dirSong) and (os.access (dirSong, os.R_OK and os.W_OK)))
	
	def createList (self, dirSong, dirList):
		""" Reads the files of dirSong into a file and write it into dirList """
		song_list = []
		os.chdir (dirSong)
		for files in glob.glob (os.path.join (".", "*.mp3")):
			song_list.append(files[2:-4])
		
		os.chdir (dirList)
		f = open ("song-list.txt", "w")
		for song in song_list:
			f.write (song)
			f.write ("\n\r")
		
		f.close ()
		
		print "OK, FATTO!"
	
	pass
