'''
Instrutions:


The starter code provides you with the main menu for a command-line
based grocery list application.

The user should be able to add, update, and remove items.

Small exercise ------------------------------------------------
Using this starter code, you're going to combine the pieces of code
you've written so far to create the functionality for each action (either 
adding, updating, or removing an item).

Each time the user adds, updates, or deletes an item, they should see the main menu again.

Medium exercise ------------------------------------------------
For each sub-menu, show the user another menu with choices for that section of the application.
For example, when Removing Items, show the user this menu:

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu

If they enter "2", prompt them for the index of the item to delete.
If they enter "3", prompt them for a start index and an end index for the slice to delete.

After deleting, show them the "delete" menu again.
To return to the main menu, the user needs to enter "4" at the prompt.

Large exercise ------------------------------------------------
Add a second array that stores whether or not each grocery list item has been obtained.
Every time you add or remove an item, you need to add to or remove from this second list.

Add an additional main menu option for changing the status of any grocery list item.

Update the "Print Items" output so that it shows whether or not an item has been obtained.
'''


groceries = []
completed = []

main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Update Status
6. Quit

'''
edit_menu = '''

1. Print items
2. Edit an item
3. Edit multiple items
4. Return to main menu

'''
delete_menu = '''

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu

'''
status_menu = '''

1. Print items
2. Update an item
3. Update multiple items
4. Return to main menu

'''
while True:
    menu_choice = int(input(main_menu))
    # Add if/else statements for each menu item
    if menu_choice == 1:
        if groceries == []:
            print("The list is empty! Select Option 2 to start adding items.")
        else:
            # Print the grocery list with indexes
            indexes = range(len(groceries))
            for i in indexes:
                if completed[i]:
                    item = groceries[i]
                    print(f'{i}: {item}: ✅')
                else:
                    item = groceries[i]
                    print(f'{i}: {item}: ✔️')
    elif menu_choice == 2:
        # Prompt for a new item until the just hit Enter
        # (meaning the didn't type anything in at the prompt)
        while True:
            item = input('What do you need from the store? (press Enter when finished) ')

            if item == '':  # Alternatively: check if len(item) == 0
                break # After we break, python will move to the next unindented line of code after the loop
            groceries.append(item)
            completed.append(False)
    elif menu_choice == 3:
        while True:
            menu_choice = int(input(edit_menu))
            if menu_choice == 1:
                # Print the grocery list with indexes
                indexes = range(len(groceries))
                for i in indexes:
                    if completed[i]:
                        item = groceries[i]
                        print(f'{i}: {item}: ✅')
                    else:
                        item = groceries[i]
                        print(f'{i}: {item}: ✔️')
            elif menu_choice == 2:
                index_to_replace = int(input('What index to replace? '))
                # Prompt the user for the new item
                new_item = input('What is the new item? ')
                # - replace the item at that index with the new item
                groceries[index_to_replace] = new_item
                completed[index_to_replace] = False
            elif menu_choice == 3:
                # Give them the chance to replace 
                start_index_to_replace = int(input('What start index to replace? '))
                end_index_to_replace = int(input('What end index to replace? '))
                # gather replacements
                replacements = []
                revised_completed = []
                while True:
                    new_item = input('What is the new item? (press Enter when finished) ')
                    if new_item == '':
                        break
                    replacements.append(new_item)
                    revised_completed.append(False)
                    groceries[start_index_to_replace:end_index_to_replace] = replacements
                    completed[start_index_to_replace:end_index_to_replace] = revised_completed
            else:
                break
    elif menu_choice == 4:
        while True:
            menu_choice = int(input(delete_menu))
            if menu_choice == 1:
                # Print the grocery list with indexes
                indexes = range(len(groceries))
                for i in indexes:
                    if completed[i]:
                        item = groceries[i]
                        print(f'{i}: {item}: ✅')
                    else:
                        item = groceries[i]
                        print(f'{i}: {item}: ✔️')
            elif menu_choice == 2:
                del_index = int(input('What index number should we remove? '))
                del groceries[del_index]
            elif menu_choice == 3:
                start_index = int(input('What is the starting index of the item you want to remove? '))
                endex = int(input('What is the ending index of the item you want to remove? '))
                del groceries[start_index:endex]
            elif menu_choice == 4:
                break
    elif menu_choice == 5:
        while True:
            menu_choice = int(input(status_menu))
            if menu_choice == 1:
                # Print the grocery list with indexes
                indexes = range(len(groceries))
                for i in indexes:
                    if completed[i]:
                        item = groceries[i]
                        print(f'{i}: {item}: ✅')
                    else:
                        item = groceries[i]
                        print(f'{i}: {item}: ✔️')
            elif menu_choice == 2:
                stat_update = int(input('Update the status of which index? '))
                # Prompt the user for the new item
                new_status = not completed[stat_update]
                # - replace the item at that index with the new item
                completed[stat_update] = new_status
            elif menu_choice == 3:
                # Give them the chance to replace 
                start_index = int(input('Update the status starting where? '))
                endex = int(input('Update the status ending where? '))
                # gather replacements
                revised_completed = []
                counter = endex - start_index
                while 0 <= counter:
                    new_item = not completed[counter]
                    revised_completed.append(new_item)
                    counter -= 1
                completed[start_index:endex] = revised_completed
            else:
                break
    if menu_choice == 6:
        break
print('Thank you for using the grocery list app!')