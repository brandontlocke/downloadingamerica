
#!/usr/bin/env python

import json, re, urllib.request

chronam = input("What is the results URL you want to download?")
results = input("How many results are there?")

with urllib.request.urlopen(chronam+'&rows='+results+'&format=json') as json_file:  
    data = json.loads(json_file.read().decode())
    for p in data['items']:
        filename = p['date']+'_'+p['title']+'_'+"pg"+p['page']
        file = open(re.sub('[^a-zA-Z0-9_]', '', filename)+".txt", "w")
        file.write(p['ocr_eng'])
file.close()