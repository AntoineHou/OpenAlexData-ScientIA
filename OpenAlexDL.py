# %%
import os 
from datetime import datetime
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI')
from Dowloander_List_ID import *
from print_logo import *

print_logo()

DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"  
ID = 'C10138342'
OWERWRITE = False

PAPER_API = {
    'name': "Paper",
    'path': "https://api.openalex.org/works?filter=concept.id:",
    'content': 'Paper metadata'
}

def download_api(api, ID,  first_page, last_page):
    print("download API {} , page {}".format(api['name'], str(last_page)))
    downloader = Downloader(api, ID, DATA_DIR,
                            overwrite=OWERWRITE, delay=0)
    tnow = datetime.now()
    print ("start download API {} / {}".format(api['name'], str(tnow)))
    downloader.download(first_page , last_page)
    print('success {}'.format(str(c)))
    return c

now = datetime.now()
download_api(PAPER_API, ID, 1, 7616)
print("done in {}".format(datetime.now() - now))
