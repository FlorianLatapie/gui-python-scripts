import csv

# Defining variables
line = 0
res = []
res_text = ""

file_name_1 = "EV1.csv"
file_name_2 = "excel.csv"

row_to_search_1 = 5
row_to_search_2 = 2

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

        # Delete useless characters
        val1 = row1[row_to_search_1].replace("/", " ").replace("	", " ").replace("  ", " ")
        val2 = row2[row_to_search_2].replace("/", " ").replace("	", " ").replace("  ", " ")

        if val1 != val2:
            res_text += (
                    str(line) + "\nEV1  :" + val1 + "\nexcel:" + val2 + "\n\n")  # Faster than print() every time
            res.append([line, val1, val2]);
print(res_text)

# Save the result in a .csv file
# newline='' because "writerow" adds a newline by default
with open('res.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    for row in res:
        csv_writer.writerow(row)
