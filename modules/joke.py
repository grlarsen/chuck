# module to handle request funcitons

import requests as re

class Joke:
    BASE_URL = 'https://api.chucknorris.io/jokes/'

    def __init__(self) -> None:
        # init methods:
        self.get_categories()
        self.current = 'Chuck Norris Facts'

    def req(self, endpoint=None):
        '''GET-request for the Chuck Norris IO API'''
        if not endpoint:
            endpoint = 'random'
        
        if endpoint not in ['random', 'categories']:
            endpoint = f'random?category={endpoint}'
        
        res = re.get(self.BASE_URL + endpoint).json()
        return res
    
    def get(self, enpoint=None):
        self.current = self.req(enpoint)['value']
        # self.current = self.current.split(' ')
        # words = len(self.current)
        # inserts = words // 8
        # for i in range(1,inserts+1):
        #     self.current.insert(i*10, '\n')
        # self.current = ' '.join(self.current)
                
        
        
    def get_categories(self):
        self.categories = {
            str(key+1): value
            for key, value
            in enumerate(self.req('categories'))
        }

# debug section:
if __name__ == '__main__':
    joke = Joke()
    joke.get('animal')