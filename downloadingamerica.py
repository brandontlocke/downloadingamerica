
#!/usr/bin/env python
import json, re, urllib.request, csv, datetime

#request the url to retrieve
chronam = input("Paste in the URL for the ChronAm search results you want to download: ")

#requests the URL in json with 200 rows and adds the page number
with urllib.request.urlopen(chronam+'&format=json') as json_file:
    data = json.loads(json_file.read().decode())

#this creates a metadata csv, adds a header, grabs 20 items at a time from the API, cycles through each item and writes a row in metadata and creates a text file with the OCR. After it's done all 20, it goes back for the next 20.

#sets base variables to track the current page of json results & number of items with ocr_eng
pg=1
textcounter=0
#creates a loop that continues until the final group of 20 json results have come in
while data['endIndex'] < data['totalItems']:
    #creates metadata.csv file and writes a header the first time through
    with open('metadata.csv', 'a') as metadata:
        metawriter = csv.writer(metadata, delimiter=',')
        if pg==1:
            metawriter.writerow(['file', 'title', 'date', 'edition', 'page', 'sequence', 'city', 'county', 'state', 'page_url'])
        #loads a set of 20 results from the api and puts them in the variable 'data'
        with urllib.request.urlopen(chronam+'&rows=20&format=json&page=' + str(pg)) as json_file:
            data = json.loads(json_file.read().decode())
        json_file.close()

        #loop through each item in the json request
        for p in data['items']:
            file='notext'
            #if there's ocr_eng in the item, it creates a filename and writes to text; if not, it skips to the metadata file
            if 'ocr_eng' in p:
                #this takes the edition from the id because some pages have the same edition and sequence but unique URLS
                edition=re.search('(?<=\/ed-)(.*)(?=\/seq-)', p['id'])
                ed=edition.groups()
                sequence=re.search('(?<=\/seq-)(.*)(?=\/)', p['id'])
                seq=sequence.groups()
                #create a filename that has only letters, numbers, underscores and is formatted YYYYMMDD_title_edition_sequence.txt
                filename = re.sub('[^a-zA-Z0-9_]', '', str(p['date'])+'_'+p['title']+'_'+ str(ed) + '_'+ str(seq)) + '.txt'
                #open a text file and print the contents of ocr_eng
                file = open(filename, "w")
                file.write(p['ocr_eng'])
                #count every file with ocr_eng so that it can be compared to the folder
                textcounter+=1
            #write metadata to the csv
            metawriter.writerow([filename, p['title'], p['date'], p['edition'], p['page'], p['sequence'], p['city'][0], p['county'][0], p['state'][0], 'https://chroniclingamerica.loc.gov' + p['id']])
    pg+=1

#creates a readme with some very simple information about the corpus
with open('readme.txt', 'w') as readme:
    readme.write("Downloaded: " + str(datetime.datetime.now()) + '\n\n' + "Num of results: " + str(data['totalItems']) + " newspaper pages—" + str(textcounter) + " of those pages had OCR files. \n\n" + "Search URL: " + chronam + '\n\n' + "Search results in JSON: " + chronam + "&format=json" + '\n\n')
    search = chronam.split("&")
    first = search[0].split("?")
    readme.write("===Search terms=== " + '\n' + first[1] + 'n')
    for term in search[1:]:
        readme.write(term + '\n')
    readme.write("\n===Compiled with===\nDownloadingAmerica\nhttps://github.com/brandontlocke/downloadingamerica ")
