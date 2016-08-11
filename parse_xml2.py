import xml.etree.cElementTree as ET
import os
import sys

# python parse_xml2.py report.xml
if __name__ == "__main__":
    path_delete = sys.argv[1] #'report.xml'

    XML_FILE = os.path.join(os.getcwd(), path_delete)
    try:
        tree = ET.ElementTree(file=XML_FILE)
        root = tree.getroot()
        for test_case in root.findall('testcase'):
            skipped = test_case.find('skipped')
            if skipped != None:
                if 'Bug' not in skipped.text:
                    root.remove(test_case)
        tree.write(XML_FILE)
    except IOError as e:
        print 'nERROR - cant find file: %sn' % e
