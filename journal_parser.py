class PaperParser ():

    def __init__ (self) -> None :
        self.keys = []
    
    def check_file(self ,dict_from_json ) : 
        if len(dict_from_json) != 0 : 
            return True 
    
    

    def parse_data (self , dict_from_json ) -> Any :
        return self.parse_paper(dict_from_json  )