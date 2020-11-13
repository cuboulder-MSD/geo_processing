# -*- coding: utf-8 -*-
import sys, re, uuid, glob, requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import copy, uuid, random
from datetime import datetime
from pathlib import Path



# def removeColons(root):
#
#     return root

def addIdentifierField(root):
    ns = {'mods':'http://www.loc.gov/mods/v3'}
    potentialArk = root.find('mods:identifier[@type="ark"]',ns)
    if potentialArk is None:

        arkID = SubElement(root, 'mods:identifier')
        # print(arkID)
        arkID.set('type', 'ark')
        arkID.text = 'https://ark.colorado.edu/ark:4754/5'


        xmlstr = ET.tostring(root, encoding='utf8', method='xml')
        # print(xmlstr)
    return sync_tree(root)

def addARK(root):
    ns = {'mods':'http://www.loc.gov/mods/v3'}
    for ark in root.findall('mods:identifier[@type="ark"]',ns):

        arkURL = ark.text

        r = requests.get(arkURL)
        if r.status_code == 404:
            # print(file)
            for url in root.findall('mods:location/mods:url',ns):
                url = url.text
                arkRequest = 'https://ark.colorado.edu/ark:/?query={"filter":{"resolve_url":"'+url+'"}}'
                arkGet = requests.get(arkRequest)
                rjson = arkGet.json()
                if not rjson['results']:
                    print(file)
                if rjson['results']:
                    arkID = rjson['results'][0]['ark']
                    fullARK = 'https://ark.colorado.edu/ark:/'+ arkID
                    ark.text = fullARK
            # print(ark.text)
        if r.status_code == 200:
            ark.text=ark.text
        # print(arkURL)

    return root



        # https://ark.colorado.edu/ark:/?query={"filter":{"resolve_url":"https://geo.colorado.edu/catalog/47540-5c6b05ba4103e0000bc42274"}}
        # https://ark.colorado.edu/ark:/?query=%7B%22filter%22:%7B%22metadata.mods.titleInfo.title%22:%22BLM%20-%20Colorado%20Geothermal%20Leases%22%7D%7D

def sync_tree(tree):
    return ET.fromstring(ET.tostring(tree, encoding="utf-8", method="xml"))

def main():
    parser = ET.XMLParser(encoding="utf-8")

    p = Path("/Users/erra1244/Desktop/geolibrary-master/")

    # file_list = [f for f in p.iterdir() if f.is_file()]
    myList = []
    for file in p.glob('*.xml'):

        ns = {'mods':'http://www.loc.gov/mods/v3'}
        ET.register_namespace('mods',"http://www.loc.gov/mods/v3")
        tree=ET.parse(file,ET.XMLParser(encoding='utf-8'))
        root=tree.getroot()

        root = addIdentifierField(root)
        addARK(root)
        # print(newFile)


        for x in root.findall('mods:identifier[@type="ark"]',ns):
            myList.append(x)

            newURL = x.text.replace('https://ark.colorado.edu/ark:/','mods_') + '.xml'
            newURL = newURL.replace('/', '_')
        # newFile = 'mods_' + str(uuid.uuid4()) +'.xml'
            tree.write(newURL, xml_declaration=True,encoding='utf-8',method='xml')
    print(len(myList))
# make this a safe-ish cli script
if __name__ == '__main__':
    # print(tree)

    main()
