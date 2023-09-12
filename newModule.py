import time as t


def printDate():
    print("今天是", t.localtime()[0], "/",
        t.localtime()[1], "/", t.localtime()[2])
