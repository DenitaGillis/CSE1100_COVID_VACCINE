# CSE1100_COVID_VACCINE

#Hello everyone please enter your share of 
the program here
**#Question 1 Khushal/Ajay**

dose= str((input ("Is this your first or second dose:\n")))
dose= str((input ("Is this your first or second dose:\n")))
if dose == "First" or "first" or "Second" or "second":
    if dose in ("First", "first"):
        print ("You have chosen First dose")
  ####################AJAY AND KUSHAL################# PLEASE TEST THIS PART ASAP THE NAME PART PLEASE, This is q1 the NAME part, we only want it to accept letters not numbers
    First = input("Enter your First Name:")
while First.isalpha() is False:
 print("Only text is allowed in name please try again:")
 First= input("Enter your first name:")
Last= input("Enter your last name:")
while Last.isalpha() is False:
  print("Only text is allowed please try again:")
  Last= input("Enter your first name:")
else:
 print(First,Last)
################################################ 
    
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
