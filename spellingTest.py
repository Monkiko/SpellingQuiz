#!/usr/bin/python3
"""
The purpose of this program is to create a Spelling Test document by pulling from the Simplified_Lists created from the Quizzes.


Created by: Ian Rivera-Leandry
Created on: May 3, 2026
Last Updated: May 3, 2026
Version 1.0.0
"""

import os
from time import sleep
from random import shuffle
from unittest import case
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import RGBColor

# Get input from the user for the grade level of the desired spelling test and pass result to readSpellingQuizzes function
def start():
    grade_level = str(input("Please indicate the grade level of the spelling test (i.e. K, 1, 2, 3, etc.):  "))
    test_number = str(input("Please indicate the test number (i.e. 1, 2, 3, etc.):  "))

    if len(grade_level) == 1:
        match grade_level.lower():
            case "k":
                grade = "Kindergarten"
            case "1":
                grade = "First_Grade"
            case "2":
                grade = "Second_Grade"
            case "3":
                grade = "Third_Grade"
            case "4":
                grade = "Fourth_Grade"
            case "5":
                grade = "Fifth_Grade"
            case "6":
                grade = "Sixth_Grade"
            case "7":
                grade = "Seventh_Grade"
            case "8":
                grade = "Eighth_Grade"
        readSimplifiedLists(grade, test_number)

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


def readSimplifiedLists(grade, test_number):
    folder_path = f'Tests/{grade}/Simplified_Lists'
    files = os.listdir(folder_path)
    
    if len(files) % 4 == 0:
        match test_number:
            case "1" | "2":
                for quiz in range(1, 5):
                    filename = f"Spelling_List_#{quiz}.txt"
                    if os.path.exists(f"{folder_path}/{filename}"):
                        with open(f"{folder_path}/{filename}", "r") as simplified_list:
                            if case == "1":
                                spellingList = []
                                for line_num, line in enumerate(simplified_list):
                                    if line_num >= 5:
                                        break
                                    print(f"{line_num}: {line.strip()}")
                                
                                spellingList = simplified_list.readlines()
                                print(spellingList)
                            elif case == "2":
                                spellingList = []
                                spellingList = simplified_list.readlines()
                                print(spellingList)
                        simplified_list.close()
                

start()