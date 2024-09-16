"""
The purpose of this program is to pull an indicated number of random words from a specified spelling list and write them to a new file while removing them from the original list.


Created by: Ian Rivera-Leandry
Last Updated: September 15, 2024
Version 2.0.0
"""



import os
from time import sleep
from random import shuffle
import re


# Get input from the user for the grade level of the desired spelling list and pass result to readSpellingList function
def start():
    grade_level = str(input("Please indicate the grade level spelling list you want (i.e. K, 1, 2, 3, etc.):  "))

    if len(grade_level) == 1:
        readSpellingList(grade_level)

    else:
        clean()
        print("Incorrect Input. Please enter either K, 1, 2, 3, etc.")
        sleep(3)
        start()


# Clear the screen dependent on host OS system
def clean():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


# Read the spelling list file for the grade level indicated previous and add the contents to a list for output printing
def readSpellingList(grade):
    
    if grade.lower() == "k":
        with open("Spelling_Lists/kindergartenList.txt", "r") as spelling_file:
            spellingList = []
            spellingList = spelling_file.readlines()

        spelling_file.close()

    shuffle(spellingList)
    clean()
    printSpellingList(spellingList, grade)


def printSpellingList(list, grade):
    
    for i in range(10):
        print(str(i + 1) + ') ' + list[i], end=' ')

    listCleanUp(list, grade)


def listCleanUp(fullList, grade):

    cleanlist = fullList[10:]
    
    if grade.lower() == "k":
        with open("Spelling_Lists/kindergartenList.txt", 'w') as f:
            for i in cleanlist:
                f.writelines([i])
    
        f.close()


start()