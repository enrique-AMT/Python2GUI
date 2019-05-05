#   Import Tkinter class for window creation.
import Tkinter
#   Import helper class for file open dialog. Refer to Helper.py in the source folder for more information.
from source.Helper import Helper

window = Tkinter.Tk()


#   Helper Functions
#       Set the program to run when button is pressed...
def button_cmd():
    #   Read file from helper class
    filename = Helper().fileRead()
    #   Open file within Python for reading
    file = open(filename, "r")
    #   Create window to display file info
    new_window = Tkinter.Tk()
    #   Set window title
    new_window.title("File info")
    #   Check if file is readable; if so, read contents of file and display within new window
    if file.mode == 'r':
        new_label = Tkinter.Label(new_window, text = file.read()).pack()

#   Main class for project
if __name__ == '__main__':
    #   set the window title with this code
    window.title("GUI Test 1.0a")

    #   Add text inside the window

    label = Tkinter.Label(window, text="testing...").pack()

    button = Tkinter.Button(text="Select File", command=lambda: button_cmd()).pack()

    #   Start the window interface...
    window.mainloop()