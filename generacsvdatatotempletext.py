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
def prt(p):
    
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#--------------------------------------------------------------------------
#------------------------------------------------------------------  

initialdirectoryconfig = 'initialization.py'
#---------------------------------------------------------------
getdirectory = check_output([sys.executable, initialdirectoryconfig], universal_newlines=True)

mydownloadir = N.join(removen(getdirectory).split(N))

#--------------------------------------------------------------------------
mylist = [mydownloadir,"Ind_googlengine_states_ut_master.csv" ]
indiastautfile = fullyqualifydirs(mylist)

print(indiastautfile)

path = Path(indiastautfile)
if not path.is_file():
    pi="\'India states and UT CSV is missing!\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    exit(1)
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

