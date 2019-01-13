
#loading json into memory.
import json
data = json.load(open('classificationH4.json'))
results = data["results"]     #getting 'results' node of the hieararchical data.
outputDict = {}
for item in results:          #iterating through the results items to build out new dictionary
    id = item["id"]
    text = item["text"]
    if "meat" in text:      #yields only items which contain 'meat'
        outputDict[id] = text
print(outputDict)

#exporting dictionary to flat csv file
import csv
with open('output-items-contains-meat.csv', 'w') as csvfile:
    mywriter = csv.writer(csvfile,delimiter='|', lineterminator="\n")
    mywriter.writerows(outputDict.items())
