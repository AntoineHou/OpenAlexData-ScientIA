import json 
import requests
import os

class Downloader:
    def __init__(self, api, field_id, data_dir="./data", overwrite=False, delay=0):
        self.api_name = api['name']
        self.api_path = api['path']
        self.data_dir = data_dir
        self.overwrite = overwrite
        self.delay = delay
        self.field_id = field_id
        self.compteur = 1
        self.cursor = '*'

    def build_path(self):
        return self.data_dir+'/download/'+self.api_name + '/' +self.field_id
    
    def create_url (self  ) :
        if "C" in self.field_id : 
            return self.api_path + str(self.field_id) + '&cursor=' + str(self.cursor)
        else :
            return self.api_path + "C" + str(self.field_id) + '&cursor=' + str(self.cursor)
    
    def call_api (self ) : 
        url = self.create_url()
        print('\t call get on {}'.format(url))
        r = requests.get(url)
        data = r.json()
        return data
    
    def write_json(self, data):
        for i in range(0, data['meta']['per_page']):
            id = data['results'][i]['id'].split('W')[1]
            basedir = self.build_path()
            if not os.path.exists(basedir + '/' +str(id)):
                print('\t mkdirs {}'.format(basedir))
                os.makedirs(basedir + '/' +str(id))
            outpath = basedir+'/'+ str(id) + '/' +str(id)+'.json'
            with open(outpath, 'w') as outfile:
                print('\t write to {}'.format(outpath))
                json.dump(data['results'][i], outfile)
    
    def download(self,  first_page , last_page):
        for i in range(first_page, last_page, 1):
            if i < last_page :
                    skip = False
                    if not self.overwrite:
                        outpath = self.build_path() + '/' + str(self.field_id)
                        if os.path.exists(outpath):
                            print('\t check overwrite for {}'.format(outpath))
                            skip = os.path.exists(outpath)
                    if skip :
                        print('\t skip {}'.format(self.field_id))
                    else :
                        print('\t download {}'.format(self.field_id))
                        print('\t call api for {} on id {}'.format(
                            self.api_name, self.field_id))                
                        data = self.call_api()
                        self.write_json(data)
            self.compteur += 1
            self.cursor = data['meta']['next_cursor']
