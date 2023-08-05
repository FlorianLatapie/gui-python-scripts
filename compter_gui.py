from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import tkinter.messagebox
import compter
import csv

# Globals

file_chosen = False

export_file_chosen = False
export_file_name = None

file_name = None
row_to_search = None
has_header = False


# Functions

def open_file_chooser():
    filename = askopenfilename()
    path_label.config(text=filename)
    global file_chosen
    file_chosen = True

    global file_name
    file_name = filename


def open_file_chooser_export():
    # https://www.tutorialspoint.com/save-file-dialog-box-in-tkinter
    filename = asksaveasfile(initialfile="result.csv", defaultextension=".csv",
                             filetypes=[("All Files", "*.*"), ("CSV", "*.csv")]).name
    export_path_label.config(text=filename)
    global export_file_chosen
    export_file_chosen = True

    global export_file_name
    export_file_name = filename


def check_col_number():
    val = col_num.get()
    if not val.isnumeric():
        return False

    global row_to_search
    row_to_search = int(val) - 1
    return True


def check_has_header():
    global has_header
    has_header = not has_header
    return has_header


def launch():
    if not (file_chosen and check_col_number()):
        return False
    try:
        compter.run(file_name, row_to_search, has_header)
        return True
    except:
        return False


def lancer_afficher():
    if not launch():
        tkinter.messagebox.showinfo('Erreur', 'Vérifiez les informations entrées')
        return
    if len(compter.get_errors()) >= 20:
        tkinter.messagebox.showinfo('Erreur', "Trop d'erreurs a afficher, veuillez les sauvegarder dans un fichier")
        return

    tkinter.messagebox.showinfo('Résultat', compter.error_text())


def launch_and_save():
    if not launch() and export_file_chosen:
        tkinter.messagebox.showinfo('Erreur', 'Vérifiez les informations entrées')
        return
    with open(export_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        errors = compter.get_errors()

        csv_writer.writerow(["Numéro de ligne", "Ligne entière"])
        for row in errors:
            print(row)
            csv_writer.writerow(row)
        tkinter.messagebox.showinfo('Résultat', "Sauvegardé !")


# Main program

def run():
    root = Tk()
    root.resizable(False, False)
    root.title('Compter')

    window_width = 500
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    label = Label(root, text="Compter", font=("Segoe UI", 25), pady=10)
    label.pack()
    desctiption_label = Label(root,
                              text="Ce logiciel lit un fichier .csv, avec les valeurs séparées par un ; \net renseigne si des nombres ne se suivent pas dans une colonne donnée.\n")
    desctiption_label.pack()

    openfile = Button(root, text="Choisir fichier", command=open_file_chooser)
    openfile.pack()

    label = Label(root, text="Fichier choisi :")
    label.pack()
    global path_label
    path_label = Label(root, text="Aucun fichier choisi")
    path_label.pack()

    spacer = Label(root, text="")
    spacer.pack()

    label = Label(root, text="Donnez le numéro de la colonne à compter (A=1, B=2 ...)")
    label.pack()

    global col_num
    col_num = Entry(root, width=10)
    col_num.pack()

    comporte_des_entetes_checkbox = Checkbutton(root, text='Le fichier comporte des en-têtes',
                                                command=check_has_header)
    comporte_des_entetes_checkbox.pack()

    spacer = Label(root, text="")
    spacer.pack()

    button = Button(root, text="Lancer", command=lancer_afficher)
    button.pack()

    spacer = Label(root, text="")
    spacer.pack()

    openfile = Button(root, text="Choisir emplacement fichier a exporter", command=open_file_chooser_export)
    openfile.pack()

    label = Label(root, text="Fichier choisi pour exporter :")
    label.pack()

    global export_path_label
    export_path_label = Label(root, text="Aucun fichier choisi")
    export_path_label.pack()

    spacer = Label(root, text="")
    spacer.pack()

    button = Button(root, text="Lancer et enregistrer le resultat dans un csv", command=launch_and_save)
    button.pack()

    spacer = Label(root, text="")
    spacer.pack()

    # button = Button(root, text="Quitter", command=root.destroy)
    # button.pack()

    root.mainloop()


### Auto run program

if __name__ == "__main__":
    run()
