def phone_number():
    
    x = input("Enter your phone number:")
    print("{}-{}-{}".format(x[:3],x[3:6],x[6:]))
    
phone_number()

