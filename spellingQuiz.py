"""
The purpose of this program is to pull an indicated number of random words from a specified spelling list and write them to a new file while removing them from the original list.


Created by: Ian Rivera-Leandry
Last Updated: January 31, 2024
Version 2.0.0
"""



import os
from time import sleep
from random import shuffle

def start():
    grade_level = str(input("Please indicate the grade level spelling list you want (i.e. K, 1, 2, 3, etc.):  "))

    if len(grade_level) == 1:
        readSpellingList(grade_level)

    else:
        clean()
        print("Incorrect Input. Please enter either K, 1, 2, 3, etc.")
        sleep(3)
        start()


def clean():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def readSpellingList(grade):
    
    if grade.lower() == "k":
        with open("Spelling_Lists/kindergartenList.txt", "r") as spelling_file:
            spellingList = []
            spellingList = spelling_file.readlines()

        spelling_file.close()

    shuffle(spellingList)
    clean()

    i = 0
    while i < 10:
        print(spellingList)
        i += 1


start()