# Input two lists from user
list1 = input("Enter elements of first list (separated by space): ").split()
list2 = input("Enter elements of second list (separated by space): ").split()

# Compare lists
if list1 == list2:
    print("The two lists are equal.")
else:
    print("The two lists are not equal.")