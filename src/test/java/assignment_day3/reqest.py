#https://cataas.com/cat

import requests

def writeFile(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
        
url = 'https://cataas.com/cat?json=true'
data = requests.get(url)
print(data.json()['tags'])


#writeFile('cat.png',str(data.content))