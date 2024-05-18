# module to handle text i/o and 
from modules.joke import Joke
import time

class Menu:
    def __init__(self) -> None:
        self.active = {}
        self.joke = Joke()
        self.input = None
        self.menu_level = None

        # init methods:
        self.start_menu()

    # Input handlers
    def get_input(self):
        self.input = input('input something: ')
    
    def eval_input(self):
        if self.input not in self.active.keys():
            print(f'\n{self.input} is not a valid option')
            return False
        return True

    # Header
    def facts(self):
        print('\nChuck Norris Facts!')

    # Menus
    def start_menu(self):
        self.menu_level = 'start'
        self.active = {
            '1': 'Random fact',
            '2': 'Select category',
            'q': 'Quit'
        }
    
    def do_over_menu(self):
        self.active = {
            '1': 'One more fact',
            '2': 'Previous menu',
            'q': 'Quit'
        }

    # Print method
    def print_active_menu(self):
        for key, value in self.active.items():
            print(f'[{key}]: {value}')

    # Main methods
    def get_random_joke(self):
        self.menu_level = 'random'
        self.joke.get('random')
        
    def get_selection(self):
        self.menu_level = 'select'
        self.active = self.joke.categories
        self.active['b'] = 'back'

    def get_category_joke(self):
        self.menu_level = self.category
        self.joke.get(self.category)
        time.sleep(2)
        
    # Render method
    def update(self):
        if self.input == 'q':
            quit()

        if self.menu_level == 'start':
            if not self.eval_input():
                return
            if self.input == '1': # RANDOM JOKE
                self.get_random_joke()
                self.do_over_menu()
                return
            if self.input == '2': # SELECT CATEGORY
                self.get_selection()
                return

        if self.menu_level == 'random':
            if not self.eval_input():
                return
            if self.input == '1': # ONE MORE JOKE
                self.get_random_joke()
                self.do_over_menu()
            elif self.input == '2': # BACK TO START MENU
                self.start_menu()

        if self.menu_level == 'select':
            if not self.eval_input():
                return
            if self.input != 'b':
                self.category = self.active[self.input]
                self.get_category_joke()
                self.do_over_menu()
                return
            else:
                self.start_menu()
        
        if self.menu_level == self.category:
            if not self.eval_input():
                return
            if self.input == '1':
                print('I am here!')
                time.sleep(1)
                self.get_category_joke()
                self.do_over_menu()
                return

            elif self.input == '2':
                self.get_selection()
                
                
            
                
