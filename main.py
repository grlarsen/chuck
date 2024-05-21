#!/usr/bin/env python3
# test creating a simple GUI for chuck norris Facts
import tkinter as tk

from argparse import ArgumentParser
from modules.menu import Menu

parser = ArgumentParser()
parser.add_argument('-c', '--cli', action='store_true')
args = parser.parse_args()

class Gui:
    def __init__(self) -> None:
        # general setup
        self.menu = Menu()
        self.window = tk.Tk()
        
        # GUI objects
        self.frames = []
        self.buttons = []

        # init methods:
        self.general_setup()
        
    def general_setup(self):
        # set title of application
        self.window.title(self.menu.header)
        # configure row properties
        self.window.rowconfigure(0, minsize=640, weight=1)
        # configure column properties
        self.window.columnconfigure(1, minsize=480, weight=1)
    
    def command(self, event):
        '''this updates the frames'''
        self.menu.input = event
        self.menu.update()
        
        # Render the new frames
        self.render_buttons()
        self.render_lables()
    
    def render_buttons(self):
        '''updated dynamically'''
        # add frames
        self.frm_buttons = tk.Frame(
            self.window,
            relief=tk.RAISED,
            bd=2,
            background='black',
            )

        # place frame in window
        self.frm_buttons.grid(row=0, column=0, sticky='ns')

        # add buttons
        for key,value in self.menu.active.items():
            btn = tk.Button(
                self.frm_buttons,
                text=value,
                command=lambda key=key: self.command(key),
                height=1, width=20,
                # background='black',
                )
            self.buttons.append(btn)
        
        # button placement in frame
        for i,btn in enumerate(self.buttons):
            btn.grid(row=i, column=0, sticky='ew', padx=5, pady=5)

    def render_lables(self):
        '''updated dynamically'''
        # add frame
        self.frm_output = tk.Label(
            self.window,
            text=self.menu.joke.current,
            foreground='white',
            background='black',
            wraplength=400,
            
            )
        
        # place frame in window
        self.frm_output.grid(row=0, column=1, sticky='nsew,')

    def run(self):
        # render frames
        self.render_buttons()
        self.render_lables()

        # main loop
        self.window.mainloop()

class Cli:

    def __init__(self) -> None:
        self.menu = Menu(cli=True)

    def run(self):
        # render everything:
        while True:
            self.menu.run()
        # pass

if __name__ == '__main__':
    if args.cli:
        main = Cli()
        main.run()

    else:
        main = Gui()
        main.run()