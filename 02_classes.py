"""
Write a program that asks for the names of all of the classes you are taking this semester
Save these class names in a list.
Print all the items in the list, one per line.
"""

def classes(more_classes="y",class_list=[]):
    #Wild experiment using recursion. Not very readable, but v concise.
    class_list.append(input("Enter a name of a class you are taking this semester:\n"))
    print("\n".join(class_list)) if input("Do you have more classes to enter? (y/N):\n").strip().lower() == "n" \
    else classes(more_classes,class_list)


if __name__ == "__main__":
    classes()
