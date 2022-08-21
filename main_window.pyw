from tkinter import *
import os
import re
import importlib

# Constants
list_directory = os.listdir()
list_directory.remove(os.path.basename(__file__))
regex = re.compile(r'.+_gui\.py$')
list_directory = [i for i in list_directory if regex.match(i)]


# Methods
def launch_window(script_name):
    root.destroy()
    python_script = importlib.reload(importlib.import_module(script_name[:-3]))  # remove ".py" extension
    python_script.run()


# Creating the window
root = Tk()
root.title('Lanceurs de scripts python')

window_width = 500
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

label = Label(root, text="Choisissez le script que vous voulez exécuter")
label.pack()
spacer = Label(root, text="")
spacer.pack()

# Generating the list of scripts (buttons)
for filename in list_directory:
    Button(root, text=filename.capitalize()[:-7], command=lambda arg1=filename: launch_window(arg1)).pack()
    spacer = Label(root, text="")
    spacer.pack()

button = Button(root, text="Quitter", command=root.destroy)
button.pack()

root.mainloop()
