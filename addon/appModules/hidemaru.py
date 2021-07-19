#appModules/hidemaru.py
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2012 Masamitsu Misono


"""App module for Hidemaru Editor
"""


import appModuleHandler
from NVDAObjects.window import DisplayModelEditableText

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName=="HM32CLIENT" and obj.windowControlID==100:
			try:
				clsList.remove(DisplayModelEditableText)
			except ValueError:
				pass

