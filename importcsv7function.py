# https://pythonspot.com/reading-csv-files-in-python/
# https://pythonspot.com/category/database/
# https://pythonspot.com/en/mysql-with-python
# https://pythonspot.com/en/python-database-postgresql/
# https://jakevdp.github.io/PythonDataScienceHandbook/03.10-working-with-strings.html


import csv
import pandas as pd

def readMyFile(filename):
    column1 = []
    column2 = []
    column3 = []
    column4 = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=';')
        for row in csvReader:
            column1.append(row[0])
            column2.append(row[1])
            column3.append(row[2])
            column4.append(row[3])


    return column1, column2, column3, column4


servers, ports , databases, users = readMyFile('ALLPRIVILEGESModifyMySQL3col.csv.txt')
names = pd.Series(users)
usersip=names.str.split('@')

print(servers)
print(ports)
print(databases)
# print(users)
print(usersip)
