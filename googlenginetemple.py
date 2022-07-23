"""
Purpose : Google Connect is a utility to connect to the Google Search Engine.
Generate the csv data based on the search query given in the argument.
The demostrated program generate the datasheet in  a format in CSV.

Design and developed by :
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Nature Labs @ GCP
How to use
------------
python googlengine.py https://www.googlengine.com/tnt

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
Email           :  ramamurthy.valavandan@kyndryl.com
GCP Contact     : gcpguild@gmail.com
Date            : June 8 2022.
Contributors    : 42 key members from GCP Guild.
"""

from posixpath import split
import requests, re, csv, sys

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np
import os
import sys
from subprocess import check_output
from pathlib import Path
import webbrowser 

#--------------------------------------------------------------------------
import json, re, csv, unicodedata, string, sys, glob
from pathlib import Path
import pandas as pd
from subprocess import check_output
N="\\"
#---------------------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        clean_string = [re.sub(r'[^a-zA-Z,=":_0-9\\]+','', clean_string)]
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#-----------------------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------------------
def sorryfilemissing(necessaryfile):
        pi="\'File is missing ! \' :"
        p = ("{} {}".format(pi,necessaryfile))
        print(p)
        exit(1)
#-------------------------------------------------------------------------
#------------------------------------------------------------------  

initialdirectoryconfig = 'initialization.py'
#---------------------------------------------------------------
getdirectory = check_output([sys.executable, initialdirectoryconfig], universal_newlines=True)

mydownloadir = N.join(removen(getdirectory).split(N))

print(mydownloadir)
#--------------------------------------------------------------------------
def prt(p):
    
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#--------------------------------------------------------------------------

cities = ['Mumbai', 
'New Delhi', 
'Chennai', 
'Kolkata',
'Bengaluru',
'Hyderabad']

colheader = ['Temple Name', 
'State', 
'Description', 
'Location',
'Coordinates']

suffix = pd.DataFrame(columns=cities).add_prefix('Distance From ').columns.tolist()
suffix = pd.DataFrame(columns=suffix).add_suffix(' (Km) ').columns.tolist()

colheader = colheader + suffix

print(colheader)

#-----------------------------------------------------------------------

#########################################################################
rootpath = "C:"
client_name = "google"
Project_ID = "serpapi"
Project_Performed_Country = "indias"
projectname = "temples"
N = "\\"
applicationstatename = 'geturltest.py'


cities = ['Mumbai', 
'New Delhi', 
'Chennai', 
'Kolkata',
'Bengaluru',
'Hyderabad']

colheader = ['Temple Name', 
'State', 
'Description', 
'Location',
'Coordinates',
'Distance From Mumbai(Km)',
'Distance From NewDelhi(Km)', 
'Distance From Chennai(Km)', 
'Distance From Kolkata(Km)',
'Distance From Bengaluru(Km)',
'Distance From Hyderabad(Km)']

-------------------------------------------------
Application_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,projectname))
Google_application = ("{}{}{}".format(Application_Folder,N,applicationstatename))
Application_Data_Folder = ("{}{}{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,'data',N,projectname.capitalize()))
#------------------------------------------------------------------------------------
path = Path(Google_application)
if not path.is_file():
    pi="\'Unable to get Google URL!\' :"
    p = ("{} {}".format(pi,Google_application))
    print(p)
    exit(1)

searchpg = check_output([sys.executable, Google_application], universal_newlines=True)

gourl = re.sub(r'^.+/([^/]+)$', r'\1', searchpg)

clean_string = re.sub(r"[^a-zA-Z]+", '', gourl)
googletempledata = ("{}{}{}{}{}{}".format(Application_Data_Folder,N,projectname,"_",clean_string,".csv"))


inputtemplepath = Path(googletempledata)
if not inputtemplepath.is_file():
    pi="\'inputtemplepath is missing!\' :"
    p = ("{} {}".format(pi,inputtemplepath))
    print(p)
    exit(1)


if not searchpg:
    print ('URL missing', searchpg)
    exit(1)

print ('input', inputtemplepath)

df_temples = pd.read_csv(googletempledata, header=0,
on_bad_lines='skip', 
engine="python"
)


templesget = sorted(df_temples)

templeslist =  []

for t in (templesget):
  
    if t not in templeslist:
        templeslist.append(t)
    else:
        print("Duplicate is removed", t)


def removen(string):
    clean_string = [re.sub(r"[^a-zA-Z\s+]+",'', string)]
  
    mymano = ''
    for x in clean_string:
        mymano += ''+ x
        mymano = mymano.strip()
    
    return mymano
#------------------------------------------------
genfile = ("{}{}{}{}{}{}{}{}{}{}{}{}".format(Application_Data_Folder,N,client_name.capitalize(),'_',Project_ID.capitalize(),'_', Project_Performed_Country.capitalize(),'_', projectname.capitalize(),"_",clean_string,".csv"))


def googling(search):
    url = f"https://www.google.com/search?&q={search}"
    pi="\'Google Search for :  \' :"
    p = ("{} {}".format(pi,search))
    prt(p)
    
    req = requests.get(url)
    sor = BeautifulSoup(req.text, "html.parser")
    
    temp = sor.find("div", class_='BNeawe').text
    return temp

def addingtemples(templename,templelocation):
    
    pi="\'Temple name is searching in Google  \' :"
   
    p = ("{} {}".format(pi,templename))
    prt(p)
    temples_data.append(templename)

    search = "{}{}".format(
     templelocation, 
     " which state of india ?")
    templestate = googling(search)
    temples_data.append(templestate)


    search = "'{}, {}{}".format(templename,
    templelocation,
     " temple is famous for ")
    templedescription = googling(search)

   
    templedescription = re.sub('[^A-Za-z0-9.,)()]+', ' ' , str(templedescription)).strip()
    temples_data.append(templedescription)


    temples_data.append(templelocation)

    search = "'the latitude longitude coordinates of {} {} ".format(templelocation,"India'")
    search = [re.sub(r"[^a-zA-Z]+", ' ', k) for k in search.split("\n")]
    mymano = ' '
    for x in search:
        mymano += ' '+ x
    templecoordinates = googling(str(mymano))
    if (templecoordinates): 
        templecoordinates = re.sub('[^0-9.,]+', '', templecoordinates)
        if (templecoordinates):
                templecoordinates = ("{}{}{}".format("(", templecoordinates, ")"))
               
                temples_data.append(templecoordinates)

    for city in (cities):
    
        search = "{}{}{}{}".format( 
            "\"Road kms \" ", 
        city, " to ", 
        templelocation )
        templereach = googling(search)
        
        mano = ''
        
        mano = re.findall('km', str(templereach))
        searchcomma = ''
        searchcomma = re.search('\,', str(templereach))
        if (searchcomma):
            templereach = re.sub(",", '', templereach)
            
       
        if (mano):
        
            telmano = re.findall('\(([^$]*)\)', str(templereach))
            if (telmano):
                templedist = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(telmano))]
            
            else:
                templedist = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(templereach))]
            float_lst = list(np.array(templedist, dtype = 'float'))
            chk_lst = re.findall('\[([^$]*)\]', str(float_lst))
            if (chk_lst):
                
                float_lst = (re.sub('[^0-9.]+', '', str(float_lst)))
           
            temples_data.append(float_lst)


dfd = []

for t in (templeslist):
    temples_data = []
    tn = t.split("|") if t else []
    templename = removen(tn[0])
    templelocation = removen(tn[1])

    templesdata = addingtemples(templename,templelocation)
    
    dfd.append(temples_data)


gencsv = pd.DataFrame(dfd,  columns= colheader )

gencsv.to_csv(genfile, index=False, na_rep='Unknown')

pi="\'Temple Data is generated  \' :"
p = ("{} {}".format(pi,'CSV Data'))
prt(p)

pi="\'Validate the data .. !  \' :"
p = ("{} {}".format(pi,genfile))
prt(p)