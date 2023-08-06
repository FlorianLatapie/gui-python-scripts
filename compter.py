import csv


def convert_row_to_search(row):
    if not row.isnumeric() and row.isalpha():
        row = row.upper()
        col = 0
        for c in row:
            col = col * 26 + (ord(c) - 64)
        row = col
    return int(row) - 1


def format_error_messages(errors):
    if not errors:
        return "aucune erreur"
    return '\n'.join(f"Ligne {error[0]} ({error[1]}): {error[2]}" for error in errors)


def run(file_name, row_number_to_search, has_header=False):
    errors = []

    def add_error(line_number, reason, content):
        errors.append((line_number, reason, content))

    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        if has_header:
            next(reader)

        last_num = next(reader)[row_number_to_search]

        for (i, row) in enumerate(reader):
            current_line_number = i + 2
            if not row[row_number_to_search].isnumeric():
                add_error(current_line_number, "Erreur de lecture", row)
            elif int(row[row_number_to_search]) != int(last_num) + 1:
                add_error(current_line_number, "Pas consécutif", row)

            last_num = row[row_number_to_search]
    return errors


if __name__ == "__main__":
    print(format_error_messages(run("Sample files/count - with error.csv", convert_row_to_search("2"))))
