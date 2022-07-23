#----------------------------------------------------------------------------
import json, re, csv, unicodedata, string, sys, glob, requests, shutil
from pathlib import Path
import pandas as pd
from subprocess import check_output

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
#----------------------------
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

getstatenamecode = 'stateutname.py'
#---------------------------------------------------------------
getstatename = (check_output([sys.executable, getstatenamecode], universal_newlines=True)).split(',')[0]

def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------------------
myd = removen(getdirectory)

serpapi_image_csv = ("{}{}{}{}".format(Country_performed.capitalize(), '_', getstatename, "_Google_Image_Links_SerpApi.csv"))
mylist = [getdirectory,getstatename, serpapi_image_csv ]

imglinks = fullyqualifydirs(mylist)

fields = ['Images SerApi Links']

df_imgs = pd.read_csv(imglinks, skipinitialspace=True, usecols=fields)
row_count=df_imgs.count()[0]
#--------------------------------------------------------------------

imgsget = sorted([list(row) for row in df_imgs.values])
for i in range(1,row_count):
    temple_image_url = ''
    for x in df_imgs.values[i]:
        temple_image_url += ''+ x

    imgfile = re.sub(r'^.+/([^/]+)$', r'\1', temple_image_url)

    pattern = '[?]+'
    chkimage  = re.search(pattern,imgfile)
    if (chkimage):
        getimage = ("{}{}{}".format('image_',i,'.jpg'))
       
    else:
        getimage = imgfile

    mylist = [getdirectory,getstatename,'images_files' ]

    imagedir = fullyqualifydirs(mylist)
    
    cre_directory = Path(imagedir)
    cre_directory.mkdir(parents=True, exist_ok=True)
    mylist = [imagedir,getimage]
    filename = fullyqualifydirs(mylist)


    r = requests.get(temple_image_url, stream = True)

    if r.status_code == 200:
        
        r.raw.decode_content = True
        
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        pi="\'Image sucessfully downloaded :\' :"
        p = ("{} {}".format(pi,filename))
        prt(p)

    else:
        pi="\'Image not able to download :\' :"
        p = ("{} {}".format(pi,filename))
        prt(p)