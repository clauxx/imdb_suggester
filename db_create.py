from datetime import datetime
from lxml import html
import requests
import pandas as pd
import numpy as np
import os

class Database:
    def __init__(self):
        self.page = requests.get('http://www.imdb.com/chart/top')
        self.db_name = 'database.csv'
        self.dir = "".join([os.getcwd(), '/', self.db_name])
        self.db_exists = os.path.isfile(self.dir)
        
    def db_create(self):    
        tree = html.fromstring(self.page.content)
        return tree

    def get_name(self, tree):    
        movie_titles = tree.xpath('//td[@class="titleColumn"]//a/text()')
        return movie_titles

    def get_year(self, tree): 
        years = tree.xpath('//td[@class="titleColumn"]//span/text()')
        return years

    def get_rating(self, tree):   
        ratings = tree.xpath('//td[@class="ratingColumn imdbRating"]//strong/text()')
        return ratings
    
    def zip_data(self): 
        tree = self.db_create()
        movie_data = list(zip(self.get_name(tree), self.get_year(tree), self.get_rating(tree)))
        return movie_data
        
    def create_csv(self, movie_data):    
        df = pd.DataFrame(data = movie_data, columns=['Movie', 'Year', 'Rating'])
        df['Date of Watching'] = np.nan
        df.to_csv(self.db_name, index=False)

    def main(self):
        if not self.db_exists:    
            tree = self.db_create()
            self.get_name(tree)
            self.get_year(tree)
            self.get_rating(tree)
            movie_data = self.zip_data()
            self.create_csv(movie_data)
            

creator = Database()    
creator.main()
        
