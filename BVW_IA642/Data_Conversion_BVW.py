#import openpyxl to work with an excel sheet
import openpyxl

#open the excelsheet and insert the name
wb = openpyxl.load_workbook('Old_XLSX\Fuzzy.xlsx')
sheet = wb.active

#find length of sheet
lengthOf = sheet.max_row
	
#set iterator for loop
i = 1

#loop through the data
while i != (lengthOf+1):
	#on first pass labels the data
	if i == 1:
		sheet['D1'] = "DataSent"
		sheet['E1'] = "Flag"
		sheet['F1'] = ""
		sheet['G1'] = ""
		sheet['H1'] = ""
		sheet['I1'] = ""
		sheet['J1'] = ""
		sheet['K1'] = ""
		sheet['L1'] = ""
	#all loops after first
	else:
		#establish combinedValue for data
		combinedValue = ""
		#combinedValue defined by combining data, turning any None into a " "
		if sheet['D' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['D' + str(i)].value)
		
		if sheet['E' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['E' + str(i)].value)
		
		if sheet['F' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['F' + str(i)].value)
			
		if sheet['G' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['G' + str(i)].value)
			
		if sheet['H' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['H' + str(i)].value)
		
		if sheet['I' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['I' + str(i)].value)
		
		if sheet['J' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['J' + str(i)].value)
			
		if sheet['K' + str(i)].value == None:
			pass
		else:
			combinedValue = combinedValue + str(sheet['K' + str(i)].value)
		
		#rewrite the row
		sheet['D' + str(i)] = combinedValue
		sheet['E' + str(i)] = sheet['L' + str(i)].value
		sheet['F' + str(i)] = ""
		sheet['G' + str(i)] = ""
		sheet['H' + str(i)] = ""
		sheet['I' + str(i)] = ""
		sheet['J' + str(i)] = ""
		sheet['K' + str(i)] = ""
		sheet['L' + str(i)] = ""
		#reset combinedValue
		combinedValue = ""
	#iterate Iterator
	i = i + 1
	
#save workbook, name it [originalFilename]_Processed.xlsx
wb.save("RPM_Processed.xlsx")



	
