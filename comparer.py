import csv

def format_error_messages(errors):
    if not errors:
        return "aucune erreur"
    return "\n".join(f"Ligne {error[0]} :\n{error[1]}\n{error[2]}\n" for error in errors)

def run(file_name_1, file_name_2, row_to_search_1=0, row_to_search_2=0, entire_line=False):
    errors = []

    # Open both files at the same time
    with open(file_name_1) as f1, open(file_name_2) as f2:
        reader1 = csv.reader(f1, delimiter=';')
        reader2 = csv.reader(f2, delimiter=';')

        # iterate over the two files at the same time using zip
        for (i, row) in enumerate(zip(reader1, reader2)):
            line = i + 1
            f1_row = row[0]
            f2_row = row[1]

            if entire_line:
                val1 = "[" + ", ".join(f1_row) + "]"
                val2 = "[" + ", ".join(f2_row) + "]"
            else:
                # Delete useless characters
                val1 = f1_row[row_to_search_1].replace("/", " ").replace("	", " ").replace("  ", " ")
                val2 = f2_row[row_to_search_2].replace("/", " ").replace("	", " ").replace("  ", " ")

            if val1 != val2:
                errors.append([line, val1, val2])

        return errors


def export_errors(errors, file_name):
    # Save the result in a .csv file
    # newline='' because "writerow" adds a newline by default
    with open('res.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        for row in errors:
            csv_writer.writerow(row)

if __name__ == "__main__":
    errors = run("Sample files/compare1.csv", "Sample files/compare2.csv", entire_line=True)
    print(format_error_messages(errors))
    #export_errors(errors, "res.csv")
