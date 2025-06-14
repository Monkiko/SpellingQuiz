"""
The purpose of this program is to pull an indicated number of random words from a specified spelling list and write them to a new file while removing them from the original list.


Created by: Ian Rivera-Leandry
Last Updated: June 11, 2025
Version 2.2.1
"""



import os
from time import sleep
from random import shuffle
from docx import Document
#import re


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
    
    match grade.lower():
        case "k":
            grade_list = "kindergartenList.txt"
        case "1":
            grade_list = "firstGradeList.txt"
    
    with open("Spelling_lists/" + grade_list, "r") as spelling_file:
        spellingList = []
        spellingList = spelling_file.readlines()

    spelling_file.close()

    shuffle(spellingList)
    clean()
    printSpellingList(spellingList, grade)


# Outputs the spelling list in a numbered format for easy copy/pasta to a document file
# def printSpellingList(list, grade):
    
#     for i in range(10):
#         print(str(i + 1) + ') ' + list[i], end=' ')

#     listCleanUp(list, grade)


# Creates a new Word document and writes the spelling list to it in a numbered format
def printSpellingList(list, grade):
    doc = Document()

    quiz_number = str(input("Please enter the quiz number for this spelling list: "))
    grade_level = str(input("Please enter the grade level for this spelling list: "))

    doc.add_heading('Spelling List # ' + quiz_number + ' - ' + grade_level.capitalize(), level=1)

    for i in range(10):
        doc.add_paragraph(str(i + 1) + ') ' + list[i].strip())

    doc.save('Spelling List # ' + quiz_number + ' - ' + grade_level.capitalize() + '.docx')
    print("Spelling list saved to Spelling List # " + quiz_number + " - " + grade_level.capitalize() + ".docx")

    listCleanUp(list, grade)


# Removes the words in the spelling list from the source Spelling_Lists file so words are not reused in future iterations
def listCleanUp(fullList, grade):

    cleanlist = fullList[10:]
    
    match grade.lower():
        case "k":
            grade_list = "kindergartenList.txt"
        case "1":
            grade_list = "firstGradeList.txt"
            
    with open("Spelling_lists/" + grade_list, "w") as f:
        for i in cleanlist:
            f.writelines([i])

    f.close()

start()
