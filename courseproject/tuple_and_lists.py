# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(f'Hi, suhailmemon')
    mylist=[1,2,3,4,5,6]
    print(mylist[0])
    print(mylist)
    mylist.append(7)
    print(mylist)
    mylist.pop(2)
    print(mylist)
    mytuple=(1,2,3,4,5)
    print(mytuple)
    print(mytuple[0])
    mytuple.append(9) #error. tuples are immutable. that's the difference between a list and a tuple


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
