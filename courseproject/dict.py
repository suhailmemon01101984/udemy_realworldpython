# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(f'Hi, suhailmemon')
    mydict={"BD":"bigdata course", "ML":"ml course", "java":"java course"}
    print(mydict["BD"])
    print(mydict["ML"])
    print(mydict["java"])
    mydict["spark"]="spark course"
    print(mydict["spark"])
    print(mydict)
    print(type(mydict))
    course_exist=mydict.get("spark")
    print(course_exist)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
