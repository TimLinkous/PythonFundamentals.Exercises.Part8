import os
import sys
import logging

def walk(dirname, file_handler):
    dir_contents = os.listdir(dirname)
    for items in dir_contents:
        path = os.path.join(dirname, items)
        if os.path.isdir(path):
            walk(path, file_handler)
        else:
            file_handler.write(f"{path}\n")

         


if __name__ == '__main__':
    with open("log.txt", "w") as file_handler:
        walk(".", file_handler)
        