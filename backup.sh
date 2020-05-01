#!/bin/bash
# Script to download all documents of a reMarkable
# J. Baten 20191217 Initial version

#command -v jq >/dev/null 2>&1 || { echo >&2 "I require the jq and curl program but it's not installed.  Aborting."; exit 1; }
#command -v curl >/dev/null 2>&1 || { echo >&2 "I require the curl and jq program but it's not installed.  Aborting."; exit 1; }

#echo "On the reMarkable, open the menu in the upper left corner."
#echo "Now go to 'settings'->'Storage'."
#echo "Set 'Enable USB web interface (Beta)' to "On"
#read -p "Press the Return key when you have done so"

#for ID in $( curl  http://10.11.99.1/documents/ | jq  '.[]|.ID?')
#do
  



#done

python3 ./backup.py
git commit -a -m 'remarkable backup'
git push

