from Tkinter import Tk
from tkFileDialog import askopenfilename

class Helper:
    def fileRead(self):
        #   Keeps the Tkinter window interface from opening
        Tk().withdraw()
        #   File open dialog
        filename = askopenfilename()
        return filename