import numpy as np
import random as rn
import pandas as pd
from datetime import datetime

class Recommend:
    def __init__(self):
        self.location = r'~/Documents/python/imdb_scrapper/database.csv'
        self.df = pd.read_csv(self.location)
        self.df_size = self.df.shape[0]

    def mark_as_watched(self, cp_movie):
        d = datetime.now()
        date = d.date()
        index = cp_movie.name
        print(index)
        self.df.set_value(index,'Date of Watching', date)
        self.df.to_csv('database.csv', index=False)
    
    def choose_movie(self):
        watched = []
        unwatched = []
        for i in range(self.df_size):    
            movie = self.df.ix[i]
            if(pd.isnull(movie['Date of Watching'])):
                unwatched.append(i)
            else:
                watched.append(i)
                
        if not unwatched:
            dates = []
            for i in range(len(watched)):
                ind = watched[i]
                movie = self.df.ix[ind]
                dates.append(movie['Date of Watching'])
            index = self.df['Date of Watching' == min(dates)].index.tolist()
            return self.df.ix[index[0]]
    
        else:
            un_index = rn.choice(unwatched)
            return self.df.ix[un_index]

    def main(self):
        movie = self.choose_movie()    
        print(movie)
        self.mark_as_watched(movie)
    
choose = Recommend()
choose.main()
                
        
            
            
            
    

    
    
        
        
    
