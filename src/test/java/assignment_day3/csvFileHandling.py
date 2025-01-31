import csv

def readDataFromCSV(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for data in reader:
            print(data)
            
readDataFromCSV('D:/Day3/data2.csv')

def writeDataToCSV(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        data = [
            ['flag3'	'terminalId'	'hasRiskProfile'	'riskProfileId'],
            ['Basic'	'TEAAA098'	    'No'                '342'          ],	 
            ['Business'	'TEAAA098'	    'Yes'               '222'          ],
            ['Terminal'	'TEAAA098'	    'Yes'               '1234'         ]
        ]
        #header = ['flag3'	'terminalId'	'hasRiskProfile'	'riskProfileId']
        for row in data:
            writer.writerow(row)
            
#writeDataToCSV('D:/Day3/data2.csv')

        