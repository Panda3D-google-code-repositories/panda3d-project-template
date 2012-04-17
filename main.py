# -*- coding: utf-8-*- 

#
# Import stuff in order to have a derived ShowBase extension running
# Remember to use every extension as a DirectObject inheriting class
#
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject 
from panda3d.core import *
#
# Task declaration import (uncomment to use)
#
#from direct.task import Task

#
# Default classes used to handle input and camera behaviour
# Useful for fast prototyping
#
from myCamera import *
from myInputHandler import InputHandler
from myDebug import DebugPrint
import sys,__builtin__

#
# Show FPS and use utf8 encoding
#
from pandac.PandaModules import loadPrcFileData 
loadPrcFileData("", """
text-encoding utf8
show-frame-rate-meter 1
""") 
	
class World(ShowBase):	
	def __init__(self):
		ShowBase.__init__(self)
		
		#starting all base methods
		__builtin__.myApp = self
		__builtin__.d = DebugPrint()
		__builtin__.myCamera = MyCamera()
		__builtin__.myInputHandler = InputHandler()
		
		#default config when just opened
		myCamera.mm.showMouse()
		myCamera.setUtilsActive()
		self.defineBaseEvents()
		
		self.mainScene = render.attachNewNode("mainScene")
		
		#example debug line useful when prototyping
		d.line("sandbox ready for prototyping!")
	
	def getSceneNode(self):
		return self.mainScene
		
	def defineBaseEvents(self):
		base.accept("escape", sys.exit)

w = World()
w.run()
