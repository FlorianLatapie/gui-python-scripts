import csv


def format_error_messages(errors):
    if not errors:
        return "aucune erreur"
    return '\n'.join(f"Ligne {error[0]} : {error[1]}" for error in errors)


def run(file_name, row_to_search, has_header=False):
    errors = []

    def add_error(line_number, content):
        errors.append([line_number, content])

    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        if has_header:
            next(reader)

        last_num = next(reader)[row_to_search]

        for (i, row) in enumerate(reader):
            current_line_number = i + 2

            if not isinstance(int(row[row_to_search]), int):
                add_error(current_line_number, row)
            if int(row[row_to_search]) != int(last_num) + 1:
                add_error(current_line_number, row)

            last_num = row[row_to_search]
    return errors


if __name__ == "__main__":
    print(format_error_messages(run("Sample files/count - with error.csv", 1)))
