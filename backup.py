#!/usr/bin/python3
# Script to download all documents of a reMarkable
# J. Baten 20191217 Initial version
# J. baten 20200907 Adapt to also allow WiFi connection (but unsure yet if that would work)

# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pprint import pprint,pformat
import requests
import os

print("""On the reMarkable, open the menu in the upper left corner.
Now go to 'settings'->'About'.
In the right column, below GPLv3 Compliance is WiFi and root password information.
Notice the IP address(es). 
The correct one could be 10.11.99.1. Your milage may vary.
""")

my_ip=input("Enter the IP address here: ")

result=1
while result!=0:
  result=os.system("ping " + my_ip + " -c 1 > /dev/null 2>&1")
  if result!=0:
    print("No connection to " + my_ip + " found. Can not help you. Sorry.")

base_url= 'http://' + my_ip
doc_url = base_url+ '/documents/'
download_url=base_url+ '/download/'

print("Trying " + base_url +  "/  ... ")
resp = requests.get(url=doc_url) 
data = resp.json()
for doc in data:
    print(doc["ID"])
    print(doc["VissibleName"])
    print("Downloading '"+doc["VissibleName"]+"'")
    url = download_url + doc["ID"]+"/placeholder"
    r = requests.get(url, allow_redirects=True)
    open("backups/"+doc["VissibleName"]+".pdf", 'wb').write(r.content)
