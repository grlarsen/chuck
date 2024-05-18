# module to handle level class
from modules.menu import Menu

class Level:

    def __init__(self) -> None:
        self.menu = Menu()

    def update(self):
        # render everything:
        self.menu.facts()
        self.menu.print_active_menu()
        self.menu.get_input() #just to make a breaking point
        self.menu.update()