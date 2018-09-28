
#!/usr/bin/env python
import json, re, urllib.request, csv, datetime

#request the url to retrieve
chronam = input("Paste in the URL for the ChronAm search results you want to download: ")

#requests the URL in json with 200 rows and adds the page number
with urllib.request.urlopen(chronam+'&format=json') as json_file:
    data = json.loads(json_file.read().decode())

#this creates a metadata csv, adds a header, grabs 20 items at a time from the API, cycles through each item and writes a row in metadata and creates a text file with the OCR. After it's done all 20, it goes back for the next 20.
pg=1
while data['endIndex'] < data['totalItems']:
    with open('metadata.csv', 'a') as metadata:
        metawriter = csv.writer(metadata, delimiter=',')
        if pg==1:
            metawriter.writerow(['file', 'title', 'date', 'edition', 'sequence', 'city', 'county', 'state', 'page_url'])
        with urllib.request.urlopen(chronam+'&rows=20&format=json&page=' + str(pg)) as json_file:
            data = json.loads(json_file.read().decode())
        json_file.close()
        for p in data['items']:
            file='notext'
            if 'ocr_eng' in p:
                filename = re.sub('[^a-zA-Z0-9_]', '', str(p['date'])+'_'+p['title']+'_'+ str(p['edition']) + '_' + str(p['sequence'])) + '.txt'
                file = open(filename, "w")
                file.write(p['ocr_eng'])
            metawriter.writerow([filename, p['title'], p['date'], p['edition'], p['sequence'], p['city'][0], p['county'][0], p['state'][0], 'https://chroniclingamerica.loc.gov' + p['id']])
    pg+=1

#creates a readme with some very simple information about the corpus
with open('readme.txt', 'w') as readme:
    readme.write("Downloaded: " + str(datetime.datetime.now()) + '\n\n' + "Num of results: " + str(data['totalItems']) + " newspaper pages" + '\n\n' + "Search URL: " + chronam + '\n\n' + "Search results in JSON: " + chronam + "&format=json" + '\n\n')
    search = chronam.split("&")
    first = search[0].split("?")
    readme.write("===Search terms=== " + '\n' + first[1] + 'n')
    for term in search[1:]:
        readme.write(term + '\n')
    readme.write("\n===Compiled with===\nDownloadingAmerica\nhttps://github.com/brandontlocke/downloadingamerica ")
