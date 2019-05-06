#   Import Tkinter class for window creation.
import Tkinter
#   Import module for message alert when quitting the app.
import tkMessageBox
#   Import helper class for file open dialog. Refer to Helper.py in the source folder for more information.
from Helper import Helper

window = Tkinter.Tk()


#   Helper Functions
#       Set the program to run when button is pressed...
def button_cmd():
    #   Read file from helper class
    filename = Helper().fileRead()
    #   No filename provided. A warning pops up instructing the user to select a file
    if not filename:
        tkMessageBox.showwarning("Warning", "Please choose a file.")
    else:
        #   Open file within Python for reading
        file = open(filename, "r")
        #   Create window to display file info
        new_window = Tkinter.Tk()
        #   Set window title
        new_window.title("File info")
        #   Check if file is readable; if so, read contents of file and display within new window
        if file.mode == 'r':
            Tkinter.Label(new_window, text = file.read()).pack()

#   Main class for project
if __name__ == '__main__':
    #   set the window title with this code
    window.title("GUI Test 1.0a")

    #   Add text inside the window

    label = Tkinter.Label(window, text="testing...").pack()

    #   File selector opens with this command
    button = Tkinter.Button(text="Select File", command=lambda: button_cmd()).pack()


    #   Defines behavior of the application when you click the close button.
    def close_project():
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
            exit()


    window.protocol("WM_DELETE_WINDOW", close_project)
    #   Start the window interface...
    window.mainloop()
