xml_to_csv.py
Typ elementu
Tekst
Rozmiar
2 KB (1 548 bajtów)
Wykorzystane miejsce
2 KB (1 548 bajtów)
Lokalizacja
ssd_keras
Właściciel
ja
Zmodyfikowany
18 kwi 2020 przeze mnie
Otwarty
10:43 przeze mnie
Utworzony
10:43 w aplikacji Google Drive Web
Dodaj opis
Przeglądający mogą pobierać

"""
Created on Mon Jan 15 16:15:36 2018

@author: GustavZ
"""
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(xml_path,img_path):
    xml_list = []
    for xml_file in glob.glob(xml_path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        boxes = []
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
            boxes.append(list(value[4:]))
            name = str(value[0])
          
        image = img_path + '/' + name
    
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
    for directory in ['train','eval']:
        xml_path = os.path.join(os.getcwd(), '{}/xml_files'.format(directory))
        img_path = os.path.join(os.getcwd(), '{}/images'.format(directory))
        xml_df = xml_to_csv(xml_path,img_path)
        xml_df.to_csv('{}_labels.csv'.format(directory,directory), index=None)
        print(('Successfully converted {} xml to csv.').format(directory))



if __name__ == '__main__':
    main()
