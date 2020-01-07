import os
import time
from os import listdir

print "______ _           _     _   _       _            "
print "|  ___| |         | |   | \ | |     | |           "
print "| |_  | | __ _ ___| |__ |  \| | ___ | |_ ___  ___ "
print "|  _| | |/ _` / __| '_ \| . ` |/ _ \| __/ _ \/ __|"
print "| |   | | (_| \__ \ | | | |\  | (_) | ||  __/\__ \\"
print "\_|   |_|\__,_|___/_| |_\_| \_/\___/ \__\___||___/"                                                  
print "_______________________________________________________"
print "\n"
print "Welcome to FlashNotes, the flashcard simulator to get you through college!"

your_list = "n"
useablefiles = []
os.chdir("flash_lists") #changes directory to "flash_lists" to manage files
allfiles = os.listdir(os.curdir)
for file in allfiles: #creates a list without the backup versions of files created by text editors
    if "~" not in file:  
        useablefiles.append(file)
        
def error_message():
    print "Not a valid response"

def create_flash_list():
    finished_creating = False
    print "Input the desired name for your file or type \"back\" to return to the main menu."
    while finished_creating == False:
        listname = raw_input("> ")
        if listname + ".txt" in useablefiles:
            print "That name is already taken. Why don't you try something else?"
        elif listname == "back":
            finished_creating = True
        else:
            open(listname + ".txt", 'w')
            useablefiles.append(listname + ".txt")
            print "\"%s\" is now a new flash list!" % listname
            finished_creating = True
    
def delete_flash_list():
    correct_response = False
    finished_deleting = False
    while finished_deleting == False:
        print "Choose a list to delete, or type \"back\" to go back to the main menu."
        for file in useablefiles:
            i = file
            primeName = i.split(".")
            print primeName[0]
        answer = raw_input("> ")
        if answer + ".txt" in useablefiles:
            os.remove(answer + ".txt")
            useablefiles.remove(answer + ".txt")
            print "List deleted!"
            if not useablefiles:
                check_for_files()
                correct_response = True
        elif answer == "back": 
            correct_response = True
            finished_deleting = True
        else:
            error_message()
               
def check_for_files():
    if not useablefiles:
        x = 0
        print "You don't have any lists. Would you like to create a new flash list?"
        while x == 0:
            answer = raw_input("> ")
            if answer == "yes":
                x = 1
                create_flash_list()
            elif answer == "no":
                print "Alright, thanks for using FlashNotes. Come back when you're ready to study!"
                time.sleep(3)
                quit()
            else:
                error_message()
                
def manage_list(x):
    print "You've selected " + x + ". You can \"read\" or \"edit\" this file, or, go \"back\" to the main menu"
    answer = raw_input("> ")
    return answer
                
def read_list(x):
    chosen_list = open(x + ".txt")
    count = 0
    read_again = True
    for i, line in enumerate(chosen_list):
        count += 1
    if (count%2) != 0:
        print "One of your questions does not have an answer. Omitting last line."
        count -= 1
    chosen_list.seek(0)
    qa_combine = count #could just be count
    print "Press Enter too see the answer to each query"
    while read_again == True:
        for int in range(count):
            raw_input(chosen_list.readline().rstrip('\n'))
            if qa_combine%2 == 0:
                qa_combine -= 1
            else:
                print ""
                qa_combine -= 1
        print "Would you like to review this list again?"
        correct_input = False
        while correct_input == False:
            answer = raw_input("> ")
            if answer == "Yes" or answer == "yes":
                chosen_list.seek(0)
                correct_input = True
            elif answer == "No" or answer == "no":
                correct_input = True
                read_again = False                
            else:
                error_message()

def edit_list(x):
    chosen_list = open(x + ".txt")
    count = 0
    writing = True
    for i, line in enumerate(chosen_list):
        count += 1
    chosen_list.close()
    chosen_list = open(x + ".txt", "a")
    chosen_list.seek(count)
    print "Fill the list in Q/A format as prompted. When you're finished, enter \"back\" to retun to the main menu"
    while writing == True:
        if count%2 == 0 or count == 0:
            q = raw_input("Q: ")
            if q == "back":
                return
            else:
                chosen_list.write(q + "\n")
                count += 1
        elif count%2 != 0:
            a = raw_input("A:  ")
            if a == "back":
                print "you need an answer to X before you can quit"
            else:
                chosen_list.write(a + "\n")
                count += 1
               
def choose_a_list():
    print "Here are your current flash lists. Either type the name of the list you'd like to use," \
    " \"new\" to make a new list,"
    print "\"delete\" to delete a list, or \"exit\" to close the program"
    for file in useablefiles: #Prints lists without their file type for user convinience
       i = file
       primeName = i.split(".")
       print primeName[0]
    answer = raw_input("> ")
    if answer == "exit":
        quit()
    return answer
    
def main():
    check_for_files()
    x = choose_a_list()
    print x
    if x == "new":
        create_flash_list()
    elif x == "delete":
        delete_flash_list()
    elif x + ".txt" in useablefiles:
        y = manage_list(x)
        if y == "read":
            read_list(x)
        elif y == "edit":
            edit_list(x)
        elif y == "back":
            return
        else:
            error_message()
    else:
        error_message()
         
mainmenu = True
while mainmenu == True:   
    main()
