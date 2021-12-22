# create dictionary with x(user input) items
# keys: slot number
# values: None (participant names)
# 
from functools import partialmethod
from re import match
from typing import Match


def setUp():

    while 1:
        num = input("Enter the number of participants: ")
        if num.isdigit():
           break;
        else:
            print("Invalid Input. Try again.") 

    number_of_participants = int(num)
    participants_dict = {}

    for i in range(0, number_of_participants):
        participants_dict[i] = None

    return participants_dict

def exit_app(participants_dict):
    exit()

def cancelSignUp(participants_dict):
    print("  Participant Cancellation ")
    print("===========================")
    
    while 1:

        if input("Enter 0 to go back to main menu\nEnter anything else to continue: ") == '0':
            break;

        desired_slot = slotSelectionValidation(participants_dict, "Starting slot")

        name = input("Participan Name: ")
        
        if participants_dict[desired_slot] == name:
            participants_dict[desired_slot] = None
            print(f"Success:\n{name} has been cancelled from starting slot #{desired_slot}.")
            break;
        else:
            print(f"{name} is not in that starting slot.")


def viewParticipants(participants_dict):
    print("     View Participants     ")
    print("===========================")

    desired_slot = slotSelectionValidation(participants_dict, "Starting slot")

    slots_range_max = min(desired_slot + 6, len(participants_dict))
    slots_range_min = max(desired_slot - 5, 1)

    print("\nStarting Slot: Participant")
    for i in range(slots_range_min, slots_range_max):
        if participants_dict[i] == None:
            print(f"{i}: [empty]")
        else:
            print(f"{i}: {participants_dict[i]}")



def saveChanges():
    pass


def slotSelectionValidation(participant_dict, message):
    desired_slot = input(f"{message} #[1-{len(participant_dict)}]: ")
    while 1:
        if desired_slot.isdigit() and int(desired_slot) > 0 and int(desired_slot) <= len(participant_dict):
            return int(desired_slot)
        else:
            print("Invalid input. Try again.")



# prompt for participant name and desired slot
# check if the slot is available
def signUp(participants_dict):
    print("    Participant Sign Up    ")
    print("===========================")
    name = input("Participant Name: ")

    while 1:

        desired_slot = slotSelectionValidation(participants_dict, "Desired starting slot")


        if participants_dict[desired_slot] == None:
            participants_dict[desired_slot] = name
            print(f"Success:\n{name} is signed up in the starting slot #{desired_slot}: ")
            break;
        else:
            print(f"Error:\nSlot #{desired_slot} is filled. Please try again")
    

# Menu
def mainMenu(participant_dict):
    choice = 0

    while 1:
        print("\n      Participant Menu     ")
        print("===========================")
        print("1. Sign Up")
        print("2. Cancel Sign Up")
        print("3. View Participants")
        print("4. Save Changes")
        print("5. Exit")
        

        while 1:
            user_choice = input("Enter 1-5: ")
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= 5:
                choice = int(user_choice)
                break;
            else:
                print("Invalid Input. Try again.")

        menu = [signUp, cancelSignUp, viewParticipants, saveChanges, exit_app]

        menu[choice-1](participant_dict)
        
    




def startUp():
    print(" Welcome to the Tournament ")
    print("===========================")

    participants_dict = setUp()

    mainMenu(participants_dict)







startUp()