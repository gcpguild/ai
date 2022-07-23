import pandas as pd
from pathlib import Path
import json, re, csv, unicodedata, string, sys, glob
from pathlib import Path
from subprocess import check_output
#--------------------------------------------------------------------------

N = "\\"
#-------------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-----------------------------------------------------------------
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

#---------------------------------------------------------------
initialdirectoryconfig = 'initialization.py'
#---------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))


indiastautfile = ("{}{}{}".format(getdirectory,N,"Ind_googlengine_states_ut_master.csv"))
#----------------------------------------------------------------------------------------------------
path = Path(indiastautfile)
#----------------------------------------------------------------------------------------------------
if path.is_file():
    pass
else:
    exit(1)
#---------------------------------------------------------------------------------
fields = ['States and Union Territories in India']
#----------------------------------------------------------------------------------------------------
df_stuts = pd.read_csv(indiastautfile, skipinitialspace=True, usecols=fields)
#-----------------------------------------------------
statesget = sorted([list(row) for row in df_stuts.values])
sul =  []
cap = []
templeslisings = []
#----------------------------------------------------------------------------------------------------
for t in statesget:
    m = [ x.strip() for x in ''.join(t).strip('[]').split(',') ]
    if m not in sul:
      sul.append(m[0])
      cap.append(m[1])
    else:
        print("Duplicate is removed", t)
#-----------------------------------------------------------------


csco = len(sul)
for cc in range(0,csco):
    
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', sul[cc])
  
    capital = re.sub(patternspace, '-', cap[cc])
    st = removen(statename)
    cp = removen(cap[cc])
    stc = ("{}{}{}".format(st,',',cp))
    stc = removen(stc)
    print(stc)