#!/usr/bin/env -S python3
from modules.level import Level

class Main():
    def __init__(self) -> None:
        self.level = Level()

    def run(self):
        while True:
            self.level.update()

if __name__ == '__main__':
    main = Main()
    main.run()