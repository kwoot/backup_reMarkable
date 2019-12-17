#!/usr/bin/python3
# Script to download all documents of a reMarkable
# J. Baten 20191217 Initial version

from pprint import pprint,pformat
import requests

print("""On the reMarkable, open the menu in the upper left corner.
Now go to 'settings'->'Storage'.
Set 'Enable USB web interface (Beta)' to "On"
""")

#input("Press the Return key when you have done so")

url = 'http://10.11.99.1/documents/'


resp = requests.get(url=url) #, params=params)
data = resp.json()
for doc in data:
    print(doc["ID"])
    print(doc["VissibleName"])
    print("Downloading '"+doc["VissibleName"]+"'")
    url = "http://10.11.99.1/download/"+doc["ID"]+"/placeholder"
    r = requests.get(url, allow_redirects=True)
    open(doc["VissibleName"]+".pdf", 'wb').write(r.content)
