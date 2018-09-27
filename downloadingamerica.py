
#!/usr/bin/env python
import sys, json, re, urllib.request, csv, datetime

#request the url to retrieve
chronam = input("Paste in the URL for the ChronAm search results you want to download: ")

#requests the URL in json with 200 rows and adds the page number
with urllib.request.urlopen(chronam+'&rows=200&format=json') as json_file:
    data = json.loads(json_file.read().decode()) #this .read().decode() may not be necessary
json_file.close()

#opens a metadata csv, writes a header, then for each item it creates a filename, prints the text, and prints the metadata to the csv
with open('metadata.csv', 'w') as metadata:
    metawriter = csv.writer(metadata, delimiter=',')
    metawriter.writerow(['file', 'title', 'date', 'edition', 'sequence', 'city', 'county', 'state', 'page_url'])
    for p in data['items']:
        filename = re.sub('[^a-zA-Z0-9_]', '', str(p['date'])+'_'+p['title']+'_'+ str(p['edition']) + '_' + str(p['sequence']))
        file = open(filename + ".txt", "w")
        file.write(p['ocr_eng'])
        metawriter.writerow([filename, p['title'], p['date'], p['edition'], p['sequence'], p['city'][0], p['county'][0], p['state'][0], 'https://chroniclingamerica.loc.gov' + p['id']])
metadata.close()

#if there are more than 200 rows, this will loop through the rest
pg=2
while data['endIndex'] < data['totalItems']:
    with urllib.request.urlopen(chronam+'&rows=200&format=json&page=' + str(pg)) as json_file:
        data = json.loads(json_file.read().decode()) #this .read().decode() may not be necessary
    json_file.close()
    with open('metadata.csv', 'a') as metadata:
        metawriter = csv.writer(metadata, delimiter=',')
        for p in data['items']:
            filename = re.sub('[^a-zA-Z0-9_]', '', str(p['date'])+'_'+p['title']+'_'+ str(p['edition']) + '_' + str(p['sequence']))
            file = open(filename + ".txt", "w")
            file.write(p['ocr_eng'])
            metawriter.writerow([filename, p['title'], p['date'], p['edition'], p['sequence'], p['city'][0], p['county'][0], p['state'][0], 'https://chroniclingamerica.loc.gov' + p['id']])
    metadata.close()
    pg+=1


#creates a readme with some very simple information about the corpus
with open('readme.txt', 'w') as readme:
    readme.write("Downloaded: " + str(datetime.datetime.now()) + '\n\n' + "Num of results: " + str(data['totalItems']) + " newspaper pages" + '\n\n' + "Search URL: " + chronam + '\n\n' + "Search results in JSON: " + chronam + "&format=json" + '\n\n')
    search = chronam.split("&")
    state = search[0].split("?")
    readme.write("===Search terms=== " + '\n' + state[1] + '\n' + search[1] + '\n' + search[2] + '\n' + search[3] + search[4] + '\n' + search[5] + '\n' + search[6] + '\n' + search[7] + '\n' + search[8] + '\n' + search[9] + ' & ' + search[10] + '\n\n')
    readme.write("===Compiled with===\nDownloadingAmerica\nhttps://github.com/brandontlocke/downloadingamerica ")
readme.close()
