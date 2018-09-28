import os, sys
import numpy as np
import pandas as pd

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# sets scope, credentials, client - don't mess with this
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
absPath = r'C:\Users\Anna\Downloads\Squirtudo\squirtudo\tools'
squirtClient = os.path.join(absPath, 'squirtudo-496dea56c402.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(squirtClient, scope)
client = gspread.authorize(creds)

# sheet name: squirtudo client has perms for all sheets in our shared folder
sheet = client.open('umd-gyms').sheet1

# data is a list of dicts, each of which is a row
data = sheet.get_all_records()

umdGyms = pd.DataFrame(data)

gymPotentialNames = []

for name in umdGyms['Potential Names']:
    if type(name) == str:
        name = [x.strip() for x in name.split(',')]
        if type(name) == list:
            gymPotentialNames.extend(name)
        if type(name) == str:
            gymPotentialNames.append(name)

gymPotentialNames = [x.lower() for x in gymPotentialNames]

def getLink(userinput):
    '''
    Goal: based on string from user input,
    match as closely as possible to entry in common gym names
    (are any gyms close enough to need duplicate handling?)
    then match to actual gym name
    return gmaps link
    '''
    bestRatio = 0
    bestMatch = ""
    matchedName = ""
    actualGym = pd.DataFrame()
	
    userinput = userinput.lower()

    for gymName in gymPotentialNames:
        ratio = fuzz.partial_ratio(userinput,gymName)
        if ratio > bestRatio:
            bestMatch = gymName
            bestRatio = ratio

        matchedName = bestMatch

    actualGym = umdGyms[umdGyms['Potential Names'].str.contains(matchedName)]

    mapsUrl = actualGym.iloc[0]['Maps']

    return(mapsUrl)
