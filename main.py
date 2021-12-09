import sys
import requests
from requests.auth import HTTPDigestAuth
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    url = 'http://service.vinlink.com/report?type=BASIC_PLUS&vin='
    for vin in sys.argv[1:]:
        results = requests.get(url+vin, auth=HTTPDigestAuth('login', 'password'))
        if results:
            tree = ET.fromstring(results.text)
            e = tree.findall('./REPORT/VINPOWER/VIN/DECODED/ITEM')
            for i in e:
                print('%s = %s' % (i.attrib['name'], i.attrib['value']))