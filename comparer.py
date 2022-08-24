import csv

# Defining variables
line = 0
errors = []


def error_text():
    if not errors:
        return "aucune erreur"
    text = ""
    for error in errors:
        text += f"{error[0]}\nFichier 1 : {error[1]}\nFichier 2 : {error[2]}\n\n"
    return text


def run(file_name_1, file_name_2, row_to_search_1=0, row_to_search_2=0, entire_line=False):
    global line
    line = 0

    global errors
    errors = []

    # Open both files at the same time
    with open(file_name_1) as f1, open(file_name_2) as f2:
        reader1 = csv.reader(f1, delimiter=';')
        reader2 = csv.reader(f2, delimiter=';')

        # Iterate on the shortest file to stop at the shortest file
        for row in reader1:
            line += 1
            row1 = row
            row2 = reader2.__next__()
            # Iterate on the second file at the same time as the first

            if entire_line:
                val1 = " ".join(row1)
                val2 = " ".join(row2)

                if val1 != val2:
                    errors.append([line, row1, row2])
            else:
                # Delete useless characters
                val1 = row1[row_to_search_1].replace("/", " ").replace("	", " ").replace("  ", " ")
                val2 = row2[row_to_search_2].replace("/", " ").replace("	", " ").replace("  ", " ")
                if val1 != val2:
                    errors.append([line, val1, val2])

    # Save the result in a .csv file
    # newline='' because "writerow" adds a newline by default
    with open('res.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        for row in errors:
            csv_writer.writerow(row)


if __name__ == "__main__":
    run("Sample files/compare1.csv", "Sample files/compare2.csv", entire_line=True)
    print(error_text())
