from openpyxl import load_workbook
from openpyxl import Workbook
import csv

fileToClean = "logs/betterCSV.csv"

wb = Workbook()
ws = wb.active

with open(fileToClean, 'r') as f:
	for row in csv.reader(f):
		ws.append(row)


wsRange = 502

iterator = 2

while iterator < wsRange+1:
	ws['H' + str(iterator)].value = 'no'
	iterator += 1

wsRange = 2815

while iterator < wsRange+1:
	ws['H' + str(iterator)].value = 'yes'
	iterator += 1

with open('logs/veachTest.csv', 'w', newline="") as file_handle:
    csv_writer = csv.writer(file_handle)
    for row in ws.iter_rows():
        csv_writer.writerow([cell.value for cell in row])

