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


**#Question Four (4)** David
answers = list()
age = int(input('How old are you? ')) #i will import the age variable that was set up just using this as reference.

if age > 17 and age <102:
    ques = input('Are you feeling ill today? Respond with yes or no.')
    q1 = ques.lower()

    match q1:
        case ('yes'|'no'):
            answers.append(q1)
        case _:
            q1 = input('Are you feeling ill today? ')

    ques = input('Have you ever been vaccinated for Covid-19? ')
    q2 = ques.lower()

    match q2:

        case ('yes'):
            answers.append(q2)
            
            print('1. AstraZeneca: ')
            print('2. Pfizer: ')
            print('3. Moderna: ')
            print('4. Sinopharm: ')
            print('5. Sputnik ')
                  
            ques = int(input('Type the number corresponding with the vaccine you got: '))
            match ques:
                case 1:
                    q2a = 'AstraZeneca'
                    answers.append(q2a)
                    
                case 2:
                    q2b = 'Pfizer'
                    answers.append(q2b)
                    
                case 3:
                    q2c = 'Moderna'
                    answers.append(q2c)

                case 4:
                    q2d = 'Sinopharm'
                    answers.append(q2d)

                case 5:
                    q2e = 'Sputnik V'
                    answers.append(q2e)
        
        case 'no':
                q2 = ques
                answers.append(q2)
                
        case _:
            q2 = input('Have you ever been vaccinated for Covid-19? ')

    print(answers)
else:
    exit()

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
#.............................................................................................................................................................................

#hey everyone i wrote this for Question 4, however it is running but i cant seem to get the if statement in the loop right please for some help
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Are you Feeling Sick Today?\n(a) yes\ (b) no\n\n"
    "Have you ever received a dose of the Covid 19 Vaccine?\n(a) yes\(b) no\n\n",
    "Do you have any form of Identification\n(a) yes\(b) no\n\n",
    "Do you have a history of \n(a) Myocarditis\(b) Pericarditis\(c) Bleeding Disorders\n\n",
    "Are you Currently Pregnant or Breastfeeding?\n(a) yes\(b) no\n\n",
    "Do you suffer from any condition that have compromised Your immune system such as HIV/AIDS or TB\n(a) yes\(b) no\n\n",
    "Have you undergone surgery recently?\n(a) yes\(b) no\n\n",
    "Have you ever had an allergic reaction to another vaccine(other than COVID-19 vaccine) or an injectable medication?\n(a) yes\(b) no\n\n",
    "In the last two months  received filarial prevention tablets\n(a) yes\(b) no\n\n",
    "In the last two months have you received a tetanus vaccine yellow fever vaccine\n(a) yes\ (b) no\n\n",
  ]
# THE QUESTIONS AVBOVE ARE IN AN ARRAY WHICH IS THEN STORED IN A CLASS

questions = [
     Question(question_prompts[0], "b"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "b"),
     Question(question_prompts[4], "b"),
     Question(question_prompts[5], "b"),
     Question(question_prompts[6], "b"),
     Question(question_prompts[7], "b"),
     Question(question_prompts[8], "b"),
     
]

# ABOVE IS SECOND ARRAY FOR THE QUESTION AND THE CORRECT ANSWER.

# THE FOR LOOP STATEMENT BELOW IS ONLY RUNNING THE QUESTIONS AND ACCEPTING ANSWERS, I DONT KNOW HOW TO DO AN IF STATEMENT THAT SAY IFF QUESTION_PROMPT[0] IS YES EXIT PROGRAM
# NEED SOME HELP
     

def prevax_screen(questions):
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
              print("okay")
 

prevax_screen(questions)
