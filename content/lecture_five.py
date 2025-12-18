#syntax for if elif else
if 5 > 7:
  print("5 is greater than 7")
elif 7 > 5:
  print("7 is greater than 5")
else:
  print("Invalid eqaution")


# project example
choise = input("There is a fork in the road would you like to go left or right enter 'l' for left and 'r' for right")
if choise == 'l':
    print("You went left and you see a number that says call would you like to call the number or not")
    choise = input("Enter y for yes and n for no")
    if choise =='y':
        print("You called the number and you find out you won the lottery")
    
    elif choise == "n":
        print("You did not call the number and pressed forward")
    else:
        print("Invalid option")
    

elif choise == 'r':
    print("You went right and you see your destination would you like to go in")
    choise = input("Enter y for yes or n for no")
    if choise == "y":
        print("You went in to the building a recived a prize You win")
    elif choise == "n":
        print("You decided you did not want to go in headed back home")
    else:
        print("Enter a valid choise")

else:
    print("Invalid choise")
