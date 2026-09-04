#!/usr/bin/env python3
import xml.etree.ElementTree as ET

tree = ET.parse("kjvak.xml")
root = tree.getroot()

verses=[]
books = root.findall("BIBLEBOOK")
for book in books:
    for chapter in book.findall("CHAPTER"):
        for vers in chapter.findall("VERS"):

            bnam = book.attrib.get("bname")
            bnum = book.attrib.get("bnumber")
            cnum = chapter.attrib.get("cnumber")
            vnum = vers.attrib.get("vnumber")
            text = vers.text

            verses.append((bnum,bnam,cnum,vnum,text))


verses.sort(key=lambda x: int(x[0]))

for vers in verses:
    print(f"{vers[1]}|{vers[2]}|{vers[3]}|{vers[4]}")

