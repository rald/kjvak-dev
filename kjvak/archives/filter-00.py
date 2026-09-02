#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def parse_bible_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    result_verses = []
    
    for book in root.findall('BIBLEBOOK'):
        bname = book.get('bname')
        bsname = book.get('bsname')
        bnumber = book.get('bnumber')
        chapters = book.findall('CHAPTER')
        number_of_chapters = len(chapters)
        
        verse_counts = []
        for chap in chapters:
            chapter_verses = chap.findall('VERS')
            verse_counts.append(str(len(chapter_verses)))
            
        verses_str = ",".join(verse_counts)

        result_verses.append((bname, bsname, bnumber, number_of_chapters, verses_str))
        
    return result_verses

verses = parse_bible_xml('kjvak.xml')

# Convert bnumber to int for correct numerical sorting
verses.sort(key=lambda x: int(x[2]))

for vers in verses:
    print(f"{vers[0]}|{vers[1]}|{vers[2]}|{vers[3]}|{vers[4]}")
