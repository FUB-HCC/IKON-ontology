import csv
import sys

outfile = open('kdf-definitionen.n3', 'wb')

n3writer = csv.writer(outfile,
    delimiter=' ',
    quotechar='"',
    escapechar="\\",
    doublequote=False,
    quoting=csv.QUOTE_MINIMAL
)

with open('kdf-definitionen-n3.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
    for row in csvreader:
        row.append("@de")
        row.append(".")
        n3writer.writerow(row)

