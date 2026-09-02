#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse("kjvak.xml")
root = tree.getroot()

books = []
for book in root.findall('BIBLEBOOK'):
    bnum = book.get('bnumber')
    bnam = book.get('bname')
    bsnm = book.get('bsname')

    # Converted bnum to an integer to ensure numerical sorting rather than alphabetical
    books.append((int(bnum), bnam, bsnm))

# Sort the list of tuples based on bnum (index 0)
# books.sort(key=lambda x: x[0])

for book in books:
    print(book)
