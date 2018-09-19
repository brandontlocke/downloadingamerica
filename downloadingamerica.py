
#!/usr/bin/env python

import json, re, urllib.request

#request the url to retrieve
chronam = input("What is the results URL you want to download?")

#by default, only 20 items are returned; this checks to see how many total items are there
checkrows = urllib.request.urlopen(chronam+'&format=json')
values = json.load(checkrows)
rows = values['totalItems']
checkrows.close()

#re-requests the URL with the total number of results attached
with urllib.request.urlopen(chronam+'&rows='+str(rows)+'&format=json') as json_file:
    data = json.loads(json_file.read().decode())
    for p in data['items']:
        filename = p['date']+'_'+p['title']+'_'+"pg"+p['page']
        file = open(re.sub('[^a-zA-Z0-9_]', '', filename)+".txt", "w")
        file.write(p['ocr_eng'])

file.close()
