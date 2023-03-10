
inventory = [
    {"Name": "Instrument", "Discription": "Hand tools", "Quantity": 8},
    {"Name": "Details", "Discription": "Car parts", "Quantity": 3},
    {"Name": "Hardware", "Discription": "Boolts", "Quantity": 12}
]


def add_element():
    new_element = {}
    while True:
        print("Enter Element name")
        el_name = input()
        if el_name.isalpha():
            new_element["Name"] = el_name.capitalize()
        else:
            print("You need to enter a word")
            continue
        break
    while True:
        print("Enter Element discription")
        el_discription = input()
        if el_discription.isalpha():
            new_element["Discription"] = el_discription.capitalize()
        else:
            print("You need to enter a word")
            continue
        break
    while True:

        print("Enter Quantity")
        el_quantity = input()
        if el_quantity.isdigit():
            new_element["Quantity"] = el_quantity
        else:
            print("You need to enter a digit")
            continue
        break
    return inventory.append(new_element)


def remove_element():
    print("Enter element name for remove")
    rem_element = input()
    rem_element = rem_element.capitalize()
    out = list(filter(lambda iter_dict: rem_element in iter_dict["Name"], inventory))
    inventory.remove(out[0])
    return inventory


def update_quantity():
    print("Enter element name whose quantity you want to change, then enter the new quantity")
    up_quantity = input()
    for iter_dict in inventory:
        if up_quantity.capitalize() in i["Name"]:
            new_quantity = int(input())
            iter_dict["Quantity"] = new_quantity
            break
    return inventory


def invent_search():
    print("Enter element name for search")
    el_search = input()
    el_search = el_search.capitalize()
    for iter_dict in inventory:
        if el_search in iter_dict["Name"] or el_search in iter_dict["Discription"]:
            print(i)


def tab():
    while True:
        for iter_dict in inventory:
            print(iter_dict)
        break


while True:
    print("??lick to select an action:" "\n 1 - View inventory\n 2 - Add element \n 3 - Remove element "
          "\n 4 - Update Quantity \n 5 - Inventory search \n q - Quit ")
    select_action = input()
    if select_action == 'q':
        print("Program comlited")
        break
    elif select_action == '1':
        tab()
        continue
    elif select_action == '2':
        add_element()
    elif select_action == '3':
        remove_element()
    elif select_action == '4':
        update_quantity()
    elif select_action == '5':
        invent_search()
    elif select_action == 'q':
        break
    else:
        print("You entered the wrong value")
        continue
    continue
