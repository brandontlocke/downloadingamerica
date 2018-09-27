
#!/usr/bin/env python
import sys, json, re, urllib.request, csv, datetime

#request the url to retrieve
chronam = input("Paste in the URL for the ChronAm search results you want to download: ")

#by default, only 20 items are returned; this checks to see how many total items are there
checkrows = urllib.request.urlopen(chronam+'&format=json')
values = json.load(checkrows)
rows = values['totalItems']
checkrows.close()

#re-requests the URL with the total number of results attached
with urllib.request.urlopen(chronam+'&rows='+str(rows)+'&format=json') as json_file:
    data = json.loads(json_file.read().decode())
json_file.close()

#opens a metadata csv, writes a header, then for each item it creates a filename, prints the text, and prints the metadata to the csv
with open('metadata.csv', 'w') as metadata:
    metawriter = csv.writer(metadata, delimiter=',')
    metawriter.writerow(['file', 'title', 'date', 'edition', 'sequence', 'city', 'county', 'state', 'page_url'])
    for p in data['items']:
        filename = re.sub('[^a-zA-Z0-9_]', '', p['date']+'_'+p['title']+'_'+ p['edition'] + '_' + p['sequence'])
        file = open(filename + ".txt", "w")
        file.write(p['ocr_eng'])
        metawriter.writerow([filename, p['title'], p['date'], p['edition'], p['sequence'], p['city'][0], p['county'][0], p['state'][0], 'https://chroniclingamerica.loc.gov' + p['id']])
metadata.close()

#creates a readme with some very simple information about the corpus
with open('readme.txt', 'w') as readme:
    readme.write("Downloaded: " + str(datetime.datetime.now()) + '\n\n' + "Num of results: " + str(rows) + " newspaper pages" + '\n\n' + "Search URL: " + chronam + '\n\n' + "Search results in JSON: " + chronam + "&format=json&rows=" + str(rows) + "\n\n")
    search = chronam.split("&")
    state = search[0].split("?")
    readme.write("===Search terms=== " + '\n' + state[1] + '\n' + search[1] + '\n' + search[2] + '\n' + search[3] + search[4] + '\n' + search[5] + '\n' + search[6] + '\n' + search[7] + '\n' + search[8] + '\n' + search[9] + ' & ' + search[10] + '\n\n')
    readme.write("===Compiled with===\nu'U+1F4F0DownloadingAmerica\nhttps://github.com/brandontlocke/downloadingamerica ")
readme.close()
