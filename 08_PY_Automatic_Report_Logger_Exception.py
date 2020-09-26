import pandas as pd
import glob
import os
import shutil 
import datetime
import logging

# Guideline on logging https://realpython.com/python-logging/

#Date Time
x = datetime.datetime.now()
dts = x.strftime('%Y%m%d')
print(dts)

#Create Logger
LOG_FILENAME = 'Logs_'+dts+'.log'
logger = logging.getLogger(LOG_FILENAME)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s = %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

#Create folder if not available
if not os.path.exists("output" + "/" + dts):  
    os.makedirs("output" + "/" + dts)
    logger.debug('Create Folder '+ dts + ' Success')
    
#Read content of text file, copy to one big table
all_files_program = glob.glob("input/folder_input/input*.txt")
all_data = []

try:
    for f in all_files_program:
        df = pd.read_table(f, sep = '|', dtype={'CIF':str, 'Date':str})
        all_data.append(df)
        #print(f)
        #Move file after proceed
        dest = shutil.move(f, 'output' + "/" + dts)   
    df_mf_all = pd.concat(all_data, axis = 0, ignore_index=True)
    df_mf_all.to_csv('output' + '/' + dts + '/summary_'+dts+'.txt',index=False, sep="|")
    logging.debug("Process Moving and summary is Done!!")
except IOError:
    logging.debug("Process Reading file Failed, the process has been done or something error,please check your source file first")
