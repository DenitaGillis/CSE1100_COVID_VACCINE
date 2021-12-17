# CSE1100_COVID_VACCINE

#Hello everyone please enter your share of 
the program here
**#Question 1 Khushal/Ajay**

dose= str((input ("Is this your first or second dose:\n")))
dose= str((input ("Is this your first or second dose:\n")))
if dose == "First" or "first" or "Second" or "second":
    if dose in ("First", "first"):
        print ("You have chosen First dose")
#################################################
##Program Intro - Cassie
intro = 'WELCOME TO COV-AL! \nThis program is a data collection and analysis model. \nIt collects patient demographics and medical history, then suggests a suitable vaccine based on the info you enter. \nPlease enter data as truthfully and as accurately as possible for best results.'
intro = intro.center(300)
print (intro,'\n\n')

while True:
  dose = input ('Lets get started.\nIs this your FIRST or SECOND dose of the vaccine?\n')
  dose = dose.casefold() #makes it so that the input will not be case sensitive

  first_txt = ['first','1st'] #creates a list of text/string that will be taken as valid if user choses "first" 
  second_txt = ['second','2nd'] #creates a list of text/string that will be taken as valid if user chooses "second"
 
  if any(x in dose for x in first_txt):
    choice = 'first'
    print ('You have selected that this is your FIRST dose')
    break

  elif any(x in dose for x in second_txt):
    choice = 'second' 
    print ('You have selected that this is your SECOND dose')
    break

  else:
    print ('Invalid input, please try again') 

print ('\n\n'choice) #this line is just to test the coice variable and can be disregarded or deleted

###################################################################


    First = input("Enter your First Name:") #PLEASE TEST THIS NAME PART #IT HAS BEEN TESTED
    while First.isalpha() is False:
        print("Only text is allowed in name, please try again:")
        First= input("Enter your first name:")
    Last= input("Enter your last name:")
    while Last.isalpha() is False:
        print("Only text is allowed please try again:")
        Last= input("Enter your first name:")
    
    print("Enter your date of birth (YYYY/MM/DD):")
    from datetime import datetime, date
    def calculateAge(birthDate):
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    while True:
        d=input()
        if (int(d[5:7])>=13):
            print("Please only enter months between 1 and 12:")
        elif (int(d[5:7])<1):
            print("Please only enter months between 1 and 12:")
        elif (int(d[8:])<=0):
            print("Please only enter days between 1 and 31:")
        elif (int(d[8:])>31):
            print("Please only enter days between 1 and 31:")
        elif (int(d[5:7])==2) and (int(d[8:])>29):
            print("Please only enter days between 1 and 29:")
        else:
            break
    
    year=d[0:4]
    month=d[5:7]
    day=d[8:]

    print('Your age is:')
    print(calculateAge(date(int(year),int(month),int(day))))


    gender=str(input("Enter your sex (M/F):\n"))
    race=str(input("Enter your Ethnicity:\n"))
    address=str(input("Enter your Address:\n"))
    region=input("Enter the region you are from:\n")
    email=str(input("Enter your email:\n"))
    cell_number=str((input("Enter your cell number:\n")))
    
if dose in ('Second', 'second'):
    print ("You have chosen Second dose")
    
#FIRST DOSE PROGRAM
#############################################################################################################################################################
# This is the code for questions 4 to 6. Done by Denita Gillis 

import sys
import random

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer 
  # this is a class function i use for the question prompt. the remaining pre vax question will be automatic promoted

vaccine = []
vaccine.append(["pfizer"])
vaccine.append(["moderna"])
vaccine.append(["astra zeneca"])
vaccine.append(["sputnik v"])
vaccine.append(["janssen"])
vaccine.append(["sinopharm"]) 

# Vaccines where place in a list for random choice based on the if statement at the end of the code

first_dose_vaccine = random.choice(vaccine)

age = int(input("please enter your age: "))#this will be taken from age calculator
if age < 18:
     print("You do not meet the age criteria for the covid-19 vaccine")
     sys.exit(123) #sys.exit is to stop the code from continue
else:
     print(" Please answer yes or no to the following questions or a,b,c,d when ask too,failure to do so will lead to inaccuracy")
        
Q1= input("Are you feeling sick today?")
while Q1 !="yes" and Q1 !="no":
     Q1= input("Are you feeling sick today?")
if Q1== "yes":
      print("Sorry, please return when you are feeling better")
      sys.exit(123)
else:
     print(" Let us move unto the next question")
                    
Q2= input("Have you ever recieved a dose of the Covid 19 vaccine")
while Q2 !="yes" and Q2 !="no":
      Q2= input("Have you ever recieved a dose of the covid 19 vaccine?")
if Q2== "yes":
     print("Let me swtich over to the second dose terminal")
     sys.exit(123)
else:
     print(" Let us move unto the next question") #once the user passes this phase the remaing questions will be prompted            

question_prompts = [
     "Do you have any form of indentification?class Question\n(a) yes \n(b) no  ",
     "Do you have a history of\n(a) Myocarditis\n(b) Pericarditis\n(c) Bleeding Disorders\n(d) none, please select a,b,c,or,d  ",
     "Are you currently pregnant of breast feeding?\n(a) yes \n(b) no ",
     "Do you suffer from any condition that have compromised Your immune system such as HIV/AIDS or TB?\n(a) yes \n(b) no ",
     "Have you recently undergone surgery?\n(a) yes \n(b) no  ",
     "Have you ever had an allergic reaction to another vaccine(other than COVID-19 vaccine) or an injectable medication?:\n(a) yes \n(b) no ",
     "In the last two months  received filarial prevention tablets?\n(a) yes \n(b) no  ",
     "In the last two months have you received a tetanus vaccine yellow fever vaccine? \n(a) yes \n(b) no ",
     ]

questions = [
     Question(question_prompts[0], "yes"),
     Question(question_prompts[1], "d"),
     Question(question_prompts[2], "no"),
     Question(question_prompts[3], "no"),
     Question(question_prompts[4], "no"),
     Question(question_prompts[5], "no"),
     Question(question_prompts[6], "no"),
     Question(question_prompts[7], "no"),
]

# the score and age variable is use to determine if the person get the vaccine and the type


def prevax_screen(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))   
          
     if age >=18 and age < 55 and score == 8: 
          print(" The vaccine you will be recieving today is:",first_dose_vaccine)
     elif age >=18 and age < 55 and score < 8 and score >=5:
               print("you are high risk candidate, you will recieve:", vaccine[1])
     elif age >= 55 and score <=8 and score >=5:
               print(" Your age and answers make you a prime candidate for:", vaccine[4])
     else:
          print("Based on your answers you do not meet the criteria for covid-19 vaccination")  
                   

prevax_screen(questions)





############################################################################################################################################################## 
# Hmm. Second dose ig - Bhudram Singh
# Code for Second Dosage

#First or second dose prompt
    
    def dose() :
        print("Is this your first or second dose of the Covid-19 Vaccine?")
        doseNum = input("Enter '1' for 1st dose, '2' for 2nd dose, or '0' to exit: ")
        doseValidate(doseNum)
    
    def doseValidate(doseNum) :
        if doseNum == "1" or doseNum == "2" :
            print("You entered",doseNum+".\nSo this is your",doseNum+"nd dosage?")
            doseCheck = input("Enter 'y' for yes or any other character for no: ")
            if doseCheck == "y" or doseCheck == "Y":
                if doseNum == "1" :
                   print("Return to dose 1...")
                else :
                   print()
                   input("Press Enter to proceed")
                   commonSymptoms()
            else :
                print("Please choose again.")
                dose()
        elif doseNum == "0" :
            print("Have a nice day.")
            exit()
        else :
            print("You entered an invalid character. Please choose again.")
            dose()
        
#Second dose questionnaire questions
#1
#List of common symptoms

    commonSymptomsList = {
        1:"Pain",
        2:"Redness",
        3:"Swelling",
        4:"Tiredness",
        5:"Headache",
        6:"Muscle pain",
        7:"Chills",
        8:"Fever",
        9:"Nausea"
        }

#Function displaying and inquiring if patient experienced any symptoms.
    
    def commonSymptoms() :
        print("Have you experienced any of these common symptoms after taking your first dose of the vaccine?\n",commonSymptomsList)
        commonSymptomsCheck = input("Enter 'y' for yes, 'n' for no, or '0' to exit: ")
        commonSymptomsValidate(commonSymptomsCheck)
    
#Function validating if patient has symptoms or not.
    
    def commonSymptomsValidate(commonSymptomsCheck) :
        if commonSymptomsCheck == "y" or commonSymptomsCheck == "Y" or commonSymptomsCheck == "n" or commonSymptomsCheck == "N" :
            if commonSymptomsCheck == "y" or commonSymptomsCheck == "Y" :
                print()
                commonSymptomsChoice()
            else :
                print("You have no common symptoms")
                input("Press enter to proceed.")
                rareSideEffects()
        elif commonSymptomsCheck == "0":
            print("Have a nice day.")
            exit()
        else :
            print("You entered an incorrect character. Please choose again.")
            print()
            input("Press Enter to proceed.")
            commonSymptoms()
        
#Function validating Common symptoms choices.

    def commonSymptomsChoice() :
        print("Which of these symptions have you experienced after taking your first vaccine?\n",commonSymptomsList)
        patientCommonSymptomsInt = input("Enter the numbers that corresponds to the symptoms: ")
        patientCommonSymptoms = {}
        i = 0
        for i in patientCommonSymptomsInt :
            isIInt = i.isdigit()
            if not(isIInt) or int(i) < 1 :
                print()
                print("You entered incorrect character(s).\nPlease choose again.")
                input("Press Enter to proceed.")
                commonSymptomsChoice()
            else :
                patientCommonSymptoms[int(i)] = commonSymptomsList[int(i)]
        print()
        print("Are these symptoms correct?\n",patientCommonSymptoms)
        commonSymptomsCheck = input("Enter 'y' for yes or any other character for no: ")
        if commonSymptomsCheck == "y" or commonSymptomsCheck == "Y" :
            input("Press enter to proceed.")
            rareSideEffects()
        else :
            print()
            print("You entered an incorrect symptom. Please choose again.")
            commonSymptomsChoice()

#2
#List of Rare side effects.

    rareEffectsList = {
        1:"Inflammation of the Heart or Pericardium",
        2:"Inflammation of the Middle Tissue Heart Muscle",
        3:"A Significant Type of Allergic Reaction called Anaphylaxis",
        4:"A Hypersensitivity Reaction to a Drug or Medication"
    }

#Function displaying and inquiring if patient experienced any Rare Side Effects.

    def rareSideEffects() :
        print("Have you experienced any of these rare side effects after taking your first dose of the vaccine?\n")
        i = 0
        for i in rareEffectsList :
            print(i,".",rareEffectsList[i])
        rareEffectsCheck = input("Enter 'y' for yes, 'n' for no, or '0' to exit: ")
        rareEffectsValidate(rareEffectsCheck)
    
#Function validating if patient has side effects or not.

    def rareEffectsValidate(rareEffectsCheck) :
        if rareEffectsCheck == "y" or rareEffectsCheck == "Y" or rareEffectsCheck == "n" or rareEffectsCheck == "N" :
            if rareEffectsCheck == "y" or rareEffectsCheck == "Y" :
                print()
                rareEffectsChoice()
            else :
                print("You have no rare side effects.")
                input("Press enter to proceed.")
                medicalConditions()
        elif rareEffectsCheck == "0" :
            print("Have a nice day.")
            exit()
        else :
            print("You entered an incorrect character. Please choose again.")
            print()
            input("Press Enter to proceed.")
            rareSideEffects()
        
#Function validating rare side effects choices.

    def rareEffectsChoice() :
        print("Which of these rare side effects have you experienced after taking your first vaccine?\n")
        i = 0
        for i in rareEffectsList :
            print(i,".",rareEffectsList[i])
        patientRareEffectsInt = input("Enter the numbers that corresponds to the symptoms: ")
        patientRareEffects = {}
        i = 0
        for i in patientRareEffectsInt :
            isIInt = i.isdigit()
            if not(isIInt) or int(i) > 4 or int(i) < 1:
                print()
                print("You entered incorrect character(s).\nPlease choose again.")
                input("Press Enter to proceed.")
                rareEffectsChoice()
            else :
                patientRareEffects[int(i)] = rareEffectsList[int(i)]
        print()
        print("Are these side effects correct?")
        i = 0
        for i in patientRareEffects :
            print(i,".",patientRareEffects[i])
        rareEffectsCheck = input("Enter 'y' for yes or any other character for no: ")
        if rareEffectsCheck == "y" or rareEffectsCheck == "Y" :
            input("Press enter to proceed.")
            print()
            medicalConditions()
        else :
            print()
            print("You entered an incorrect side effect. Please choose again.")
            rareEffectsChoice()

#3

    #List of conditions
    conditionsList = {
        1:"Myocarditis",
        2:"Pericarditis",
        3:"Bleeding Disorders"
    }

#Function displaying and inquiring if patient experienced any of the listed conditions

    def medicalConditions() :
        print("Have you developed any of the following conditions after taking the vaccine?\n",conditionsList)
        conditionsCheck = input("Enter 'y' for yes, 'n' for no, or '0' to exit: ")
        medicalConditionsValidate(conditionsCheck)

#Function validating if patient has the conditions.

    def medicalConditionsValidate(conditionsCheck) :
        if conditionsCheck == "y" or conditionsCheck == "Y" or conditionsCheck == "n" or conditionsCheck == "N" :
            if conditionsCheck == "y" or conditionsCheck == "Y" :
                print()
                medicalConditionsChoice()
            else :
                print("You have none of the conditions mentioned.")
                input("Press enter to proceed")
                print()
                immuneCompromised()
        elif conditionsCheck == "0":
            print("Have a nice day.")
            exit()
        else :
            print("You entered an incorrect character.\nPlease choose again.")
            input("Press enter to proceed")
            print()
            medicalConditions()

#Function specifying which condition they have

    def medicalConditionsChoice() :
        print("Which of the conditions have you experienced after taking the vaccine?\n",conditionsList)
        patientConditionsInt = input("Enter the numbers that corresponds to the conditions: ")
        patientConditions = {}
        i = 0
        for i in patientConditionsInt :
            isIInt = i.isdigit()
            if not(isIInt) or int(i) < 1 or int(i) > 3 :
                print()
                print("You entered an incorrect character.\nPlease choose again.")
                input("Press enter to proceed.")
                medicalConditionsChoice()
            else :
                patientConditions[int(i)] = conditionsList[int(i)]
        print()
        print("Are these side effects correct?\n",patientConditions)
        conditionsCheck = input("Enter 'y' for yes or any other character for no: ")
        if conditionsCheck == "y" or conditionsCheck == "Y" :
            print()
            immuneCompromised()
        else :
            print("You selected an incorrect option.\nPlease choose again.")
            input("Press enter to proceed.")
            medicalConditionsChoice()

#4
#List of immuno compromisers

    immuneCompromiseList = {
        1:"HIV/AIDS",
        2:"TB"
    }

#Function displaying and inquiring if the patient is immuno compromised

    def immuneCompromised() :
        print("Have you become immune compromised in any of the following ways?\n",immuneCompromiseList)

#Function specifying

    patientImmuneCompromisedInt = input("Enter the numbers that corresponds with the immune compromises, or enter 'n' for no, or '0' to exit: ")
    patientImmuneCompromised = {}

#Function validating choices

    i = 0
    immuneCompromise = False
    for i in patientImmuneCompromisedInt :
        isIInt = i.isdigit()
        if not(isIInt) and i == "n" or not(isIInt) and i == "N" :
            print()
            print("You do not have any immune compromises.")
            input("Press enter to proceed.")
            print()
            filarialPrevention()
        elif not(isIInt) and i != "n" or not(isIInt) and i != "N" or i < "0" or i > "2":
            print()
            print("You entered an incorrect character. Please choose again.")
            input("Press enter to proceed.")
            print()
            immuneCompromised()
        elif i == "0" :
            print()
            print("Have a great day.")
            exit()
        else :
            patientImmuneCompromised[int(i)] = immuneCompromiseList[int(i)]
            immuneCompromise = True
    if immuneCompromise :  
        print("The following immune compromises are what you selected:\n",patientImmuneCompromised)
        print("Is this correct?")
        immuneCompromisedCheck = input("Enter 'y' for yes, or any other character for no: ")
        if immuneCompromisedCheck == "y" or immuneCompromisedCheck == "Y" :
            print()
            print("You verified your selection of",patientImmuneCompromised)
            print()
            input("Press enter to proceed.")
            filarialPrevention()
        else:
            print()
            print("You selected an incorrect immune compromise.\nPlease choose again.")
            print()
            input("Press enter to proceed.")
            immuneCompromised()

#5
#Function inquiring about the reception of filarial prevention tablets 

    def filarialPrevention() :
        print("Have you received filarial prevention tablets in the past two (2) months?")
        filarialPreventionCheck = input("Enter 'y' for yes, 'n' for no, or '0' to exit: ")

#Function Verifying the reception of filarial prevention tablets

    if filarialPreventionCheck == "y" or filarialPreventionCheck == "Y" or filarialPreventionCheck == "n" or filarialPreventionCheck == "N" : 
        if filarialPreventionCheck == "y" or filarialPreventionCheck == "Y" :
            print()
            print("You have received filarial prevention tablets in the past two (2) months.")
            print()
            input("Press enter to proceed.")
            otherVaccines()
        else:
            print()
            print("You have not received filarial prevention tablets in the past two (2) months.")
            print()
            input("Press enter to proceed.")
            otherVaccines()
    elif filarialPreventionCheck == "0" :
        print()
        print("Have a great day.")
        exit()
    else :
        print()
        print("You entered an incorrect character.\nPlease choose again.")
        input("Press enter to proceed.")
        filarialPrevention()

#6
#List of other vaccines

    otherVaccinesList = {
        1:"Tetanus Vaccine",
        2:"Yellow Fever Vaccine"
    }

#Asking if patient has had other vaccines.

    def otherVaccines() :
        print("In the last two (2) months, have you received any of the following vaccines?\n",otherVaccinesList)
        patientOtherVaccinesInt = input("Enter the corresponding numbers, or 'n' for no, or '0' to exit: ")
        patientOtherVaccines = {}
        vaccinated = False
        i = 0
        for i in patientOtherVaccinesInt :
            isIInt = i.isdigit()
            if not(isIInt) and i == "n" or not(isIInt) and i == "N" :
                print()
                print("You did not receive any of the listed vaccinations in the past two (2) months.")
                input("Press enter to proceed.")
                print()
                conclude()
            elif not(isIInt) and i != "n" or not(isIInt) and i != "N" or i < "0" or i > "2":
                print()
                print("You entered an incorrect character. Please choose again.")
                input("Press enter to proceed.")
                print()
                otherVaccines()
            elif i == "0" :
                print()
                print("Have a great day.")
                exit()
            elif isIInt and int(i) > 0 or isIInt and int(i) < 3 :
                patientOtherVaccines[int(i)] = otherVaccinesList[int(i)]
                vaccinated = True
        if vaccinated :    
            print("The following vaccines are what you selected \n",patientOtherVaccines)
            print("Is this correct?")
            otherVaccinesCheck = input("Enter 'y' for yes, or any other character for no: ")
            if otherVaccinesCheck == "y" or otherVaccinesCheck == "Y" :
                print()
                print("You verified your selection of",patientOtherVaccines)
                input("Press enter to proceed.")
                print()
                conclude()
            else:
                print()
                print("You selected an incorrect vaccine.\nPlease choose again.")
                print()
                input("Press enter to proceed.")
                otherVaccines()

#Conclusion/End

    def conclude() :
       print("Have a microchip full Chirstmas(joke) and a covid free new year(hopefully)")
       print("Happy Cryslyr")
       input("Press enter to proceed/exit")
       exit()


#Initiation point
    
    dose()

