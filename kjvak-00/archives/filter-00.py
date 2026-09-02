#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def parse_bible_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    for book in root.findall('BIBLEBOOK'):
        bname = book.get('bname')
        bsname = book.get('bsname')
        bnumber = book.get('bnumber')
        chapters = book.findall('CHAPTER')
        number_of_chapters = len(chapters)
        
        verse_counts = []
        for chap in chapters:
            verses = chap.findall('VERS')
            verse_counts.append(str(len(verses)))
            
        verses_str = ", ".join(verse_counts)
        print(f"{bname}|{bsname}|{bnumber}|{number_of_chapters}|{verses_str}")

parse_bible_xml('kjvak.xml')
