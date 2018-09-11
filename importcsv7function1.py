# https://pythonspot.com/reading-csv-files-in-python/
# https://pythonspot.com/category/database/
# https://pythonspot.com/en/mysql-with-python
# https://pythonspot.com/en/python-database-postgresql/
# https://jakevdp.github.io/PythonDataScienceHandbook/03.10-working-with-strings.html

import csv

def readMyFile(filename):
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=';')
        next(csvReader)  # skip header
        for row in csvReader:
            column1.append(row[0])
            column2.append(row[1])
            column3.append(row[2])
            temp = row[3].split('@')
            column4.append(temp[0])
            column5.append(temp[1])

    return column1, column2, column3, column4, column5


servers, ports , databases, users , hosts = readMyFile('MySQLprivileges.csv.txt')

print(servers)
print(ports)
print(databases)
print(users)
print(hosts)
