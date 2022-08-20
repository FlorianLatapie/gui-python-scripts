import csv

last_number = -1
line = 0
errors = []


def get_errors():  # I'm not sure that it is correct or if there is a better way to do it
    return errors


def save_error(line_number, line_content):
    errors.append([line_number, line_content])


def error_text():
    if not errors:
        return "aucune erreur"
    text = ""
    for error in errors:
        text += f"Ligne {error[0] + 1} : {error[1]}\n"
    return text


def run(file_name, row_to_search, has_header=False):
    global line  # very ugly but it works
    line = 0

    global errors  # don't mind this either
    errors = []

    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        if has_header:
            next(reader)
            line += 1

        last_num = reader.__next__()[row_to_search]

        for row in reader:
            line += 1

            try:
                if int(row[row_to_search]) != int(last_num) + 1:
                    save_error(line, row)
            except:
                save_error(line, row)

            last_num = row[row_to_search]


if __name__ == "__main__":
    run("Sample files/count - with error.csv", 1)
    print(error_text())
