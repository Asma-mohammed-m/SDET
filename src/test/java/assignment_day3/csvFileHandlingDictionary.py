import csv

def readDataFromCSV(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for data in reader:
            print(data)
            
#readDataFromCSV(data.csv)

def writeDataToCSVDict(filename):
    with open(filename, 'w', newline='') as file:
        header = ['flag3','terminalId','hasRiskProfile','riskProfileId']
        writer = csv.DictWriter(file, fieldnames=header)
        
        data = [
            {'flag3': 'Basic' , 'terminalId': 'TEAAA098' , 'hasRiskProfile':'No'  ,'riskProfileId':'342' },	 
            {'flag3': 'Business'  ,	'terminalId': 'TEAAA098' , 'hasRiskProfile':'Yes' ,'riskProfileId':'222' },
            {'flag3': 'Terminal'  ,	'terminalId': 'TEAAA098' , 'hasRiskProfile':'Yes' ,'riskProfileId':'1234' }
        ]
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
writeDataToCSVDict('D:/Day3/data1.csv')

        