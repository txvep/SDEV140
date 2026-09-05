"""
 Create a program that leads a person through the steps of fixing a bad Wi-Fi connection.
 Here is an example of the program’s output:
 Reboot the computer and try to connect.
    Did that fix the problem? (yes/no) no
 
 reboot the router and try to connect.
    Did that fix the problem? (yes/no) no

 Notice the program ends as soon as a solution is found to the problem. 
 Here is another example of the program’s output:
 Reboot the computer and try to connect.
    Did that fix the problem? (yes/no) no

 reboot the router and try to connect.
    Did that fix the problem? (yes/no) no

 Make sure the cables between the router and modem are plugged in firmly.
    Did that fix the problem? (yes/no) no

 Move the router to a new location.
    Did that fix the problem? (yes/no) no

Get a new router.
 """


print("reboot the computer and try to connect.")
if str.lower(input("Did that fix the problem? (yes/no) ")) == "no":
    print("reboot the router and try to connect.")
    if str.lower(input("Did that fix the problem? (yes/no) ")) == "no":
        print("Make sure the cables between the router and modem are plugged in firmly.")
        if str.lower(input("Did that fix the problem? (yes/no) ")) == "no":
            print("Move the router to a new location.")
            if str.lower(input("Did that fix the problem? (yes/no) ")) == "no":
                print("Get a new router.")
