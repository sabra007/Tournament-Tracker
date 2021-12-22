# create dictionary with x(user input) items
# keys: slot number
# values: None (participant names)
# 
def setUp():

    while 1:
        num = input("Enter the number of participants: ")
        if num.isdigit():
           break;
        else:
            print("Invalid Input. Try again.") 

    number_of_participants = int(num)
    patricipants_dict = {}

    for i in range(0, number_of_participants):
        patricipants_dict[i] = None

    
    return patricipants_dict


def startUp():
    print("Welcome to the Tournament")
    print("=========================")
    participants_dict = setUp()
    







startUp()