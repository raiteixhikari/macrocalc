##### MALE BMR Function ################################################# START ####

def mbmr(age,height,weight):
    return round(66 + (13.7 * weight) + (5 * height) - (6.8 * age),2)

##### MALE BMR Function ################################################# END ####

##### FEMALE BMR Function ############################################### START ####

def fbmr(age,height,weight):
    return round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age),2)

##### FEMALE BMR Function ############################################### END ####


##### TDEE Maintenance and Cut Based on MALE BMR ############################################ START ####

def msedentary(mbmr):
    return round((mbmr(age,height,weight) * 1.2),2)

def msedentarycut(msedentary):
    return round(msedentary(mbmr) - ((20/100) * msedentary(mbmr)),2)

def mlight(mbmr):
    return round((mbmr(age,height,weight)* 1.375),2)

def mlightcut(mlight):
    return round(mlight(mbmr) - ((20/100) * mlight(mbmr)),2)

def mmoderate(mbmr):
    return round((mbmr(age,height,weight) * 1.55),2)

def mmoderatecut(mmoderate):
    return round(mmoderate(mbmr) - ((20/100) * mmoderate(mbmr)),2)

def mvery(mbmr):
    return round((mbmr(age,height,weight) * 1.725),2)

def mverycut(mvery):
    return round(mvery(mbmr) - ((20/100) * mvery(mbmr)),2)

def mextreme(mbmr):
    return round((mbmr(age,height,weight) * 1.9),2)

def mextremecut(mextreme):
    return round(mextreme(mbmr) - ((20/100) * mextreme(mbmr)),2)

##### TDEE Maintenance and Cut Based on MALE BMR ############################################ END ####


##### TDEE Maintanance and Cut Based on FEMALE BMR ########################################## START ####

def fsedentary(fbmr):
    return round((fbmr(age,height,weight) * 1.2),2)

def fsedentarycut(fsedentary):
    return round(fsedentary(fbmr) - ((20/100) * fsedentary(fbmr)),2)

def flight(fbmr):
    return round((fbmr(age,height,weight)* 1.375),2)

def flightcut(flight):
    return round(flight(fbmr) - ((20/100) * flight(fbmr)),2)

def fmoderate(fbmr):
    return round((fbmr(age,height,weight) * 1.55),2)

def fmoderatecut(fmoderate):
    return round(fmoderate(fbmr) - ((20/100) * fmoderate(fbmr)),2)

def fvery(fbmr):
    return round((fbmr(age,height,weight) * 1.725),2)

def fverycut(fvery):
    return round(fvery(fbmr) - ((20/100) * fvery(fbmr)),2)

def fextreme(fbmr):
    return round((fbmr(age,height,weight) * 1.9),2)

def fextremecut(fextreme):
    return round(fextreme(fbmr) - ((20/100) * fextreme(fbmr)),2)

##### TDEE Maintainance and Cut Based on FEMALE BMR ########################################## END ####


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
        print("Your cutting intake is : ", msedentarycut(msedentary))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((msedentary(mbmr)+200), (msedentary(mbmr)+300)))
        input("Press Enter to continue...")

    if choice is '2':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mlight(mbmr)) #calls tdee function
        print("Your cutting intake is : ", mlightcut(mlight))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((mlight(mbmr) + 200), (mlight(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '3':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mmoderate(mbmr))  # calls tdee function
        print("Your cutting intake is : ", mmoderatecut(mmoderate))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((mmoderate(mbmr) + 200), (mmoderate(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '4':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mvery(mbmr))  # calls tdee function
        print("Your cutting intake is : ", mverycut(mvery))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((mvery(mbmr) + 200), (mvery(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '5':
        print("Your BMR is : ", mbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", mextreme(mbmr))  # calls tdee function
        print("Your cutting intake is : ", mextremecut(mextreme))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((mextreme(mbmr) + 200), (mextreme(mbmr) + 300)))
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
        print("Your cutting intake is : ", fsedentarycut(fsedentary))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((fsedentary(mbmr) + 200), (fsedentary(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '2':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", flight(fbmr))  # calls tdee function
        print("Your cutting intake is : ", flightcut(flight))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((flight(mbmr) + 200), (flight(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '3':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", fmoderate(fbmr))  # calls tdee function
        print("Your cutting intake is : ", fmoderatecut(fmoderate))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((fmoderate(mbmr) + 200), (fmoderate(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '4':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", fvery(fbmr))  # calls tdee function
        print("Your cutting intake is : ", fverycut(fvery))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((fvery(mbmr) + 200), (fvery(mbmr) + 300)))
        input("Press Enter to continue...")

    if choice is '5':
        print("Your BMR is : ", fbmr(age, height, weight))  # calls bmr function
        print("Your TDEE is :", fextreme(fbmr))  # calls tdee function
        print("Your cutting intake is : ", fextremecut(fextreme))
        # Extra Information for Bulking added here with simple addition function
        print('Your clean bulking intake is %d to %d ' % ((fextreme(mbmr) + 200), (fextreme(mbmr) + 300)))
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
