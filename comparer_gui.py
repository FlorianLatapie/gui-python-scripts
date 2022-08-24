from tkinter import *
import comparer
from tkinter.filedialog import askopenfilename


file_name_1 = None
file_name_2 = None
col1 = None
col2 = None

def open_file_chooser(label_to_update):
    filename = askopenfilename()
    label_to_update.config(text=filename)
    return filename

def launch():
    comparer.run(file_name_1, col1, file_name_2, col2)


def run():
    root = Tk()
    root.resizable(False, False)
    root.title('Comparer')

    window_width = 500
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    number_of_rows = 2
    number_of_columns = 2

    for i in range(number_of_columns):
        root.grid_columnconfigure(i, weight=1)

    label = Label(root, text="Comparer", font=("Segoe UI", 25))
    label.grid(row=0, column=0, columnspan=number_of_columns)

    label = Label(root, text="Ce logiciel lit un fichier .csv avec les valeurs séparées par un ;\net compare deux fichiers sur 2 colonnes pour vérifier qu'elles soient bien identiques.")
    label.grid(row=1, column=0, columnspan=number_of_columns)

    spacer = Label(root, text="")
    spacer.grid(row=2, column=0, columnspan=number_of_columns)

    file_name_1_button = Button(root, text="Choisir le premier fichier")
    file_name_1_button.grid(row=3, column=0)

    label = Label(root, text="Fichier choisi:")
    label.grid(row=4, column=0)

    file_name_1_label = Label(root, text="Aucun fichier choisi")
    file_name_1_label.grid(row=5, column=0)

    spacer = Label(root, text="")
    spacer.grid(row=6, column=0)

    label = Label(root, text="Colonne à vérifier (A=1, B=2 ...)")
    label.grid(row=7, column=0)

    col1_entry = Entry(root)
    col1_entry.grid(row=8, column=0)

    file_name_2_button = Button(root, text="Choisir le second fichier")
    file_name_2_button.grid(row=3, column=number_of_columns-1)

    label = Label(root, text="Fichier choisi:")
    label.grid(row=4, column=number_of_columns-1)

    file_name_2_label = Label(root, text="Aucun fichier choisi")
    file_name_2_label.grid(row=5, column=number_of_columns-1)

    spacer = Label(root, text="")
    spacer.grid(row=6, column=number_of_columns-1)

    label = Label(root, text="Colonne à vérifier (A=1, B=2 ...)")
    label.grid(row=7, column=number_of_columns-1)

    col2_entry = Entry(root)
    col2_entry.grid(row=8, column=number_of_columns-1)

    spacer = Label(root, text="")
    spacer.grid(row=9, column=0, columnspan=number_of_columns)

    launch_button = Button(root, text="Lancer", command=launch)
    launch_button.grid(row=10, column=0, columnspan=number_of_columns)

    spacer = Label(root, text="")
    spacer.grid(row=11, column=0, columnspan=number_of_columns)

    save_filename_button = Button(root, text="Choisir emplacement fichier a exporter")
    save_filename_button.grid(row=12, column=0, columnspan=number_of_columns)

    label = Label(root, text="Fichier choisi:")
    label.grid(row=13, column=0, columnspan=number_of_columns)

    save_filename_label = Label(root, text="Aucun fichier choisi")
    save_filename_label.grid(row=14, column=0, columnspan=number_of_columns)

    spacer = Label(root, text="")
    spacer.grid(row=15, column=0, columnspan=number_of_columns)

    launch_and_save_button = Button(root, text="Lancer et exporter le résultat", command=launch)
    launch_and_save_button.grid(row=16, column=0, columnspan=number_of_columns)

    root.mainloop()

if __name__ == "__main__":
    run()
