"""
The purpose of this program is to pull an indicated number of random words from a specified spelling list and write them to a new file while removing them from the original list.


Created by: Ian Rivera-Leandry
Last Updated: June 15, 2025
Version 2.2.2
"""



import os
from time import sleep
from random import shuffle
from docx import Document


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
def readSpellingList(grade_level):

    match grade_level.lower():
        case "k":
            grade = "Kindergarten"
        case "1":
            grade = "First_Grade"
    
    with open("Spelling_Lists/" + grade + "_List.txt", "r") as spelling_file:
        spellingList = []
        spellingList = spelling_file.readlines()

    spelling_file.close()

    shuffle(spellingList)
    clean()
    printSpellingList(spellingList, grade)


# Creates a new Word document and writes the spelling list to it in a numbered format
def printSpellingList(spellingList, grade):
    doc = Document()

    quiz_number = str(input("Please enter the quiz number for this spelling list: "))
    grade = str(input("Please enter the grade level for this spelling list: "))

    doc.add_heading("Spelling List # " + quiz_number + " - " + grade, level=1)

    for i in range(10):
        doc.add_paragraph(str(i + 1) + ") " + spellingList[i].strip())

    doc.save("Quizzes/" + grade + "/Spelling List #" + quiz_number + " - " + grade + ".docx")
    print("Spelling list saved to Quizzes/" + grade + "/Spelling List # " + quiz_number + " - " + grade + ".docx")

    listCleanUp(spellingList, grade)


# Removes the words in the spelling list from the source Spelling_Lists file so words are not reused in future iterations
def listCleanUp(spellingList, grade):

    cleanlist = spellingList[10:]
          
    with open("Spelling_Lists/" + grade + "_List.txt", "w") as f:
        for i in cleanlist:
            f.writelines([i])

    f.close()

start()
