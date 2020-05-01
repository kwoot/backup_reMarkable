#!/usr/bin/python3
# Script to download all documents of a reMarkable
# J. Baten 20191217 Initial version

from pprint import pprint,pformat
import requests
import os

print("""On the reMarkable, open the menu in the upper left corner.
Now go to 'settings'->'Storage'.
Set 'Enable USB web interface (Beta)' to "On"
""")

input("Press the Return key when you have done so")

result=1
while result!=0:
  result=os.system("ping 10.11.99.1 -c 1 > /dev/null 2>&1")
  if result!=0:
    print("No connection to 10.11.99.1 found")

url = 'http://10.11.99.1/documents/'


resp = requests.get(url=url) 
data = resp.json()
for doc in data:
    print(doc["ID"])
    print(doc["VissibleName"])
    print("Downloading '"+doc["VissibleName"]+"'")
    url = "http://10.11.99.1/download/"+doc["ID"]+"/placeholder"
    r = requests.get(url, allow_redirects=True)
    open("backups/"+doc["VissibleName"]+".pdf", 'wb').write(r.content)
