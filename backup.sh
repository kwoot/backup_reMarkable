#!/bin/bash
# Script to download all documents of a reMarkable
# J. Baten 20191217 Initial version

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

