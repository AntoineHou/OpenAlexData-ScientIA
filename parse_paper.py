from typing import Any

class PaperParser ():

    def __init__ (self) -> None :
        self.keys = ['id' , 'title' , 'date' ,  'authors' , 'n_citation' , 'biblio', 'concepts' , 
        'venue' , 'type' ]
    
    def check_file(self ,dict_from_json ) : 
        if len(dict_from_json) != 0 : 
            return True 

    def parse_id (self , dict_from_json ) : 
        if self.check_file(dict_from_json) : 
            try :
                return dict_from_json['id'].split('.org/')[1]
            except KeyError :
                return None
        else : 
            return None
    
    def parse_title (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                return dict_from_json['title']
            except KeyError :
                return None
        else : 
            return None
    
    def parse_date (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                return str(dict_from_json['publication_date'])
            except KeyError :
                return None
        else : 
            return None

    def parse_authors (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                authors = []
                for items in dict_from_json['authorships'] : 
                    authors.append(items['author']['id'].split('.org/')[1])
                return authors
            except KeyError :
                return None
        else :
            return None
    
    def parse_n_citation (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                return dict_from_json['cited_by_count']
            except KeyError :
                return None
        else :
            return None
    
    def parse_biblio (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                biblio = []
                # si ca marche c'est des dict donc key , value pour la boucle
                for items in dict_from_json['referenced_works'] : 
                    biblio.append(items.split('.org/')[1])
                return biblio
            except KeyError :
                return None
        else :
            return None

    def parse_concepts (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                concepts = []
                for items in dict_from_json['concepts'] : 
                    if float(items['score']) > 0.5 and len(concepts) <= 5 : 
                        concepts.append(items['id'].split('.org/')[1])
                return concepts
            except KeyError :
                return None
        else :
            return None
    
    def parse_venue (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                Venue_ID = dict_from_json['host_venue']['id'].split('.org/')[1]
                Type = dict_from_json['host_venue']['type']
                return Venue_ID , Type
            except KeyError :
                return None ,None
        else :
            return None , None


    
    def parse_paper (self , dict_from_json) :
        if self.check_file(dict_from_json) :
            paper = {}
            paper['id'] = self.parse_id(dict_from_json)
            paper['title'] = self.parse_title(dict_from_json)
            paper['date'] = self.parse_date(dict_from_json)
            paper['authors'] = self.parse_authors(dict_from_json)
            paper['n_citation'] = self.parse_n_citation(dict_from_json)
            paper['biblio'] = self.parse_biblio(dict_from_json)
            paper['concepts'] = self.parse_concepts(dict_from_json)
            Venue , Type = self.parse_venue(dict_from_json)
            paper['venue'] = Venue
            paper['type'] = Type
            return paper
        else :
            return None

    def parse_data (self , dict_from_json ) -> Any :
        return self.parse_paper(dict_from_json  )
                






