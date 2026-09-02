#!/usr/bin/env python3
import xml.etree.ElementTree as ET

tree = ET.parse("kjvak.xml")
root = tree.getroot()

books = root.findall("BIBLEBOOK")
for book in books:
    for chapter in book.findall("CHAPTER"):
        for vers in chapter.findall("VERS"):

            bnam = book.attrib.get("bname")
            cnum = chapter.attrib.get("cnumber")
            vnum = vers.attrib.get("vnumber")
            text = vers.text

            print(f"{bnam}|{cnum}|{vnum}|{text}")

