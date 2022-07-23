#----------------------------------------------------------------------------
import json, re, csv, unicodedata, string, sys, glob, requests, shutil
from pathlib import Path
import pandas as pd
from subprocess import check_output
from PIL import Image
import requests
import matplotlib.pyplot as plt
import cv2
import numpy as np
from urllib.request import urlopen
#-----------------------------------------------------------------

n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    #print(sys.argv[i], end = " ")
    arv = (sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)

N = "\\"
#---------------------------------------------------------------
initialdirectoryconfig = 'initialization.py'
#---------------------------------------------------------------
Country_performed = "indias"
#---------------------------------------------------------------------
def prt(p):
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#------------------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        clean_string = [re.sub(r'[^a-zA-Z,=":_0-9\\-]+','', clean_string)]
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#-----------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
#-----------------------------------------------------------------
getstatenamecode = 'stateutname.py'
#---------------------------------------------------------------
getstatename = (check_output([sys.executable, getstatenamecode], universal_newlines=True)).split(',')[0]

def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------------------
myd = removen(getdirectory)
#-----------------------------------------------------------------
serpapi_image_csv = ("{}{}{}{}".format(Country_performed.capitalize(), '_', getstatename, "_Google_Image_Links_SerpApi.csv"))
mylist = [getdirectory,getstatename, serpapi_image_csv ]
#-----------------------------------------------------------------
imglinks = fullyqualifydirs(mylist)
#-----------------------------------------------------------------
fields = ['Images SerApi Links']
#-----------------------------------------------------------------
df_imgs = pd.read_csv(imglinks, skipinitialspace=True, usecols=fields)
row_count=df_imgs.count()[0]
#--------------------------------------------------------------------
imgsget = sorted([list(row) for row in df_imgs.values])
for i in range(1,row_count):
    temple_image_url = ''
    for x in df_imgs.values[i]:
        temple_image_url += ''+ x
        response = requests.get(temple_image_url, stream=True)
        img = Image.open(response.raw)
        plt.figure(figsize = (20,1))
        xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()

        #plt.imshow(img, interpolation='nearest')
        plt.imshow(img, cmap='Reds', interpolation='nearest', alpha=1, extent=(xmin,xmax,ymin,ymax))   # for heatmap to overlap
        if (i ==2):
            exit(0)
        plt.show(block=False)
        plt.pause(3)
        plt.close()