from dataload import Loader
import pandas as pd


PATH = 'artifacts\breast cancer.csv'

class Clean:
    def __init__(self, path=PATH):
        self.path = path
        loader = Loader()
        self.data = loader.data_loader(self.path)
    
    def cleaning(self):
        data = self.data
        data = data.drop(["id","Unnamed: 32"], axis=1)
        data.drop_duplicates(inplace=True)
        data = data.dropna()
        data.to_csv('clean_data.csv')
        return data
