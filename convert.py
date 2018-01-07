import csv

resorts = ""

with open('nsResorts.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    resortJson = []

    for row in readCSV:

        finalJson = ",\n{\n\"type\": \"Feature\",\n\"geometry\": {\n\"type\": \"Point\",\n\"coordinates\": [\n" + row[4] + ", \n" + row[3] + "\n]\n},\n \"properties\": {\n\"marker-color\": \"#7e7e7e\",\n\"marker-size\": \"medium\",\n\"name\": \"" + row[1] + "\",\n \"description\": \"<strong>" + row[1] + "</strong><p><a href=\\\""+ row[2] +"\\\" target=\\\"_blank\\\">" + row[1] + "</a>" + row[5] + "<a href=\\\""+ row[7] +"\\\" target=\\\"_blank\\\">" + row[6] + "</a></p>\"\n}\n}"
        resortJson.append(finalJson)

    resortJson.pop(0)
    for json in resortJson:
        resorts +=str(json)

    print(resorts)
