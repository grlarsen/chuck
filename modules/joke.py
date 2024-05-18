# module to handle request funcitons

import requests as re

class Joke:
    BASE_URL = 'https://api.chucknorris.io/jokes/'

    def __init__(self) -> None:
        # init methods:
        self.get_categories()

    def req(self, endpoint=None):
        '''GET-request for the Chuck Norris IO API'''
        if not endpoint:
            endpoint = 'random'
        
        if endpoint not in ['random', 'categories']:
            endpoint = f'random?category={endpoint}'
        
        res = re.get(self.BASE_URL + endpoint).json()
        return res
    
    def get(self, enpoint=None):
        print('\n', self.req(enpoint)['value'])
        
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