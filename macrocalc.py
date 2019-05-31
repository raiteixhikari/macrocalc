##### MALE BMR Function ################################################# START ####

def mbmr(age,height,weight):
    return round(66 + (13.7 * weight) + (5 * height) - (6.8 * age),2)

##### MALE BMR Function ################################################# END ####

##### FEMALE BMR Function ############################################### START ####

def fbmr(age,height,weight):
    return round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age),2)

##### FEMALE BMR Function ############################################### END ####


##### TDEE Based on MALE BMR ############################################ START ####

def msedentary(mbmr):
    return round((mbmr(age,height,weight) * 1.2),2)

def mlight(mbmr):
    return round((mbmr(age,height,weight)* 1.375),2)

def mmoderate(mbmr):
    return round((mbmr(age,height,weight) * 1.55),2)

def mvery(mbmr):
    return round((mbmr(age,height,weight) * 1.725),2)

def mextreme(mbmr):
    return round((mbmr(age,height,weight) * 1.9),2)

##### TDEE Based on MALE BMR ############################################ END ####


##### TDEE Based on FEMALE BMR ########################################## START ####

def fsedentary(fbmr):
    return round((fbmr(age,height,weight) * 1.2),2)

def flight(fbmr):
    return round((fbmr(age,height,weight)* 1.375),2)

def fmoderate(fbmr):
    return round((fbmr(age,height,weight) * 1.55),2)

def fvery(fbmr):
    return round((fbmr(age,height,weight) * 1.725),2)

def fextreme(fbmr):
    return round((fbmr(age,height,weight) * 1.9),2)

##### TDEE Based on FEMALE BMR ########################################## END ####


##### Activity Levels Selection to calculate MALE TDEE #################################### START ####

def moption():
    print("Pick Activity Levels")
    print("1: Sedentary - Little to no exercise + desk job")
    print("2: Lightly Active - Light exercise 1-3 days/week")
    print("3: Moderately Active - Moderate exercise 3-5 days/week")
    print("4: Very Active - Heavy exercise 6-7 days/week")
    print("5: Extremely Active - Very heavy exercise,hard labor job,training 2x/day")
    print("Press q to exit")
    choice = str(input("Select Your Choice - press q to quit"))
    if choice is '1':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is : ", msedentary(mbmr)) #calls tdee function
        input("Press Enter to continue...")

    if choice is '2':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mlight(mbmr)) #calls tdee function
        input("Press Enter to continue...")

    if choice is '3':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mmoderate(mbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is '4':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mvery(mbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is '5':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mextreme(mbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is 'q':
     exit()#Quits the function
    else:
       input("Invalid Input, Press Any Key to return to options")
       moption() #once done repeats the option function until q is pressed


##### Activity Levels Selection to calculate MALE TDEE #################################### END ####


##### Activity Levels Selection to calculate FEMALE TDEE #################################### START ####

def foption():
    print("Pick Activity Levels")
    print("1: Sedentary - Little to no exercise + desk job")
    print("2: Lightly Active - Light exercise 1-3 days/week")
    print("3: Moderately Active - Moderate exercise 3-5 days/week")
    print("4: Very Active - Heavy exercise 6-7 days/week")
    print("5: Extremely Active - Very heavy exercise,hard labor job,training 2x/day")
    print("Press q to exit")
    choice = str(input("Select Your Choice - press q to quit"))
    if choice is '1':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is : ", fsedentary(fbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is '2':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", flight(fbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is '3':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", fmoderate(fbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is '4':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", fvery(fbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is '5':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", fextreme(fbmr))  # calls tdee function
        input("Press Enter to continue...")

    if choice is 'q':
        exit()  # Quits the function
    else:
        print("Invalid Input")
        foption()  # once done repeats the option function until q is pressed

##### Activity Levels Selection to calculate FEMALE TDEE #################################### END ####


##### Select Gender which will then invoke MALE or FEMALE Function ########################## START ####

def option():
    print("1: Male")
    print("2: Female")
    select = str(input("Select Your Choice - press q to quit"))
    if select is '1':
        moption()
    if select is '2':
        foption()
    if select is 'q':
        exit()
    else:
        input("Invalid Input,press any key to return to menu")
        option()

##### Select Gender which will then invoke MALE or FEMALE Function ########################## END ####


##### Initial Data Input which will lead to Gender Selection Function ############################ START ####

age = int(input("Please enter age : "))
print("You are %d years old" % (age))
height = int(input("Please enter height in cm : "))
print("You are %d cm tall" % (height))
weight = int(input("Please enter weight in kgs : "))
print("Your weight is %d kgs" % (weight))

##### Gender Selection Function ################################################################## START ####

option()

##### Gender Selection Function ################################################################## END ####

##### Initial Data Input which will lead to Gender Selection Function ############################ END ####
