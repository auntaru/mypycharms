#https://realpython.com/python-csv/
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')
            line_count += 1
        else:
            print row[0], 'works in the  ', row[1] , 'department, and was born in ', row[2]
            line_count += 1
    print('Processed {line_count} lines.')