# CSE1100_COVID_VACCINE

#Hello everyone please enter your share of 
the program here
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
