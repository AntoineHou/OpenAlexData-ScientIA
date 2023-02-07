from processor import *
from print_logo import *
import os 

print_logo()

PARSER = 'Paper'
DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"  
DIR = os.listdir(os.chdir(DATA_DIR+'/download/'+PARSER))
processor = Processor(Parser = PARSER, data_dir=DATA_DIR)
processor.process_and_write_csv(DIR)

