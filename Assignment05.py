# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Kurt Mueller>,<11.10.2019>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here

#The text file has to be pre-populated with an entry.  Was not able to fix this despite best efforts.

objFile = open("ToDoList.txt", "r")
for row in objFile:
       lstRow = row.split(",")
       dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
       lstTable.append(dicRow)
       print(dicRow)

objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here

        for objRow in lstTable:
            print(objRow)

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here

        strData1 = input("What task would you like to add?: ")
        strData2 = input("What is the priority of the task?: ")
        dicRow = {"Task":strData1 , "Priority":strData2}
        lstTable.append(dicRow)

        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
    # TODO: Add Code Here

        del lstTable[len(lstTable)-1]
        print("Last entry has been deleted...")
        print(lstTable)

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here

        objFile = open('ToDoList.txt', "w")
        for objRow in lstTable:
            objFile.write(objRow["Task"] + ',' + objRow["Priority"] + "\n")
        objFile.close()
        print("Data saved to file.")

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here

        print("You have exited the Program.")  #KRM
        break  # and Exit the program