# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 02:05:36 2019

@author: Nandita
"""

from bs4 import BeautifulSoup
import requests
import csv
import json
import pymongo


def download_csv():
    response = requests.get('https://data.gov.ie/dataset/education-t10-ed')
    W3Html = response.content

    # get soup object
    soup = BeautifulSoup(W3Html, features="html.parser")
    # get all elements with class w3-container
    download_buttons = soup.find_all(class_="dataset-resource-buttons")
    # print(W3ElementsAll)
    # Download the csv file.
    for buttons in download_buttons:
        anchor_tag = buttons.find_all('a')[-1]
        if anchor_tag:
            csv_link = anchor_tag.attrs['href']
            file_stream = requests.get(csv_link, stream=True)
            with open('kiss.csv', 'wb') as f:
                for chunk in file_stream.iter_content(chunk_size=1024 * 1024):
                    f.write(chunk)
            break

download_csv()

def convert_csv_to_joson():
    
    f = open('kiss.csv', 'r', encoding='ISO-8859-1' )
    reader = csv.DictReader(f) 
    
    jsonoutput = 'kiss.json'
    with open(jsonoutput, 'a') as f:
        for x in reader: 
            json.dump(x,f)
            f.write('\n')
        
convert_csv_to_joson()

