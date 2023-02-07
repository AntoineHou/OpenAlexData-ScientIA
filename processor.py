import os
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI')
import json 
from parse_paper import PaperParser
import pandas as pd

class Processor:
    def __init__(self, Parser = 'Paper' , data_dir="./data"):
        self.data_dir = data_dir
        if Parser == 'Paper':
            self.parser = PaperParser()
            self.api_name = 'Paper'

    def build_path(self, id):
        basedir = self.data_dir+'/download/'+self.api_name
        return basedir+'/'+id 
    
    def read_json(self, id):
        basedir = self.build_path(id)
        outpath = basedir+'/' +str(id)+'.json'
        with open(outpath, 'r') as infile:
            data = json.load(infile)
        print('\t read from {}'.format(outpath))
        return data
    
    def process(self, parser , id):
        data = self.read_json(id)
        print('\t process {}'.format(id))
        data_parsed = parser.parse_data(data)
        return data_parsed
    
    def process_list(self, list_id):
        print('\t process {} list_id'.format(len(list_id)))
        data_parsed = []
        for ids in list_id:
            data_parsed.append(self.process(self.parser, ids))
        return data_parsed
    
    def process_and_write_csv(self, list_id):
        data = self.process_list(list_id)
        outpath = self.data_dir+'/' +str(self.api_name)+'.csv'
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(outpath, index=False)
        print('\t write to {}'.format(outpath))
    