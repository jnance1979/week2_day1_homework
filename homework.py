#Option in which function requires two numbers 

def math_choice(a, b):
    while True:
        print("\nWhat mathematical operation would you like to perform?")                               
        choice = input("Enter add, subtract, multiply, or divide (or 'q' to quit) ")                # determines user operation preference
        if choice.lower() not in ('add', 'subtract' , 'multiply', 'divide', 'q'):                   # ensures valid user input
            print ("I gave you some solid options from which to pick. Now, let's try this again.")  # in case of invalid input
            continue
        elif (choice).lower() == 'q':   # ends loop upon user request
            print ("\n")
            break
        else:
            if (choice).lower() == 'add':               
                result = a + b                              # performs calculation
                print (f' {a} plus {b} = {result}.')        # prints result
            elif (choice).lower() == 'subtract':            
                result = a - b                              # performs calculation
                print (f' {a} minus {b} = {result}.')       # prints result
            elif (choice).lower() == 'multiply':
                result = a * b                              # performs calculation
                print (f' {a} times {b} = {result}.')       # prints result
            elif (choice).lower() == 'divide':
                result = a / b                              # performs calculation
                print (f' {a} divided by {b} = {result}.')  # prints result

math_choice(78, 14)


#Option in which function requires no argument. User provides the 2 numbers.
def math_choice():
    while True:
        print("\nWhat mathematical operation would you like to perform?")
        choice = input("Enter add, subtract, multiply, or divide (or 'q' to quit) ")
        if choice.lower() not in ('add', 'subtract' , 'multiply', 'divide', 'q'):
            print ("I gave you some solid options. Now, let's try this again.")
            continue
        elif (choice).lower() == 'q':
            print ("\n")
            break
        else:
            (a) = int(input("What is the first number you'd like to use? ")) # sets value of 1st number per user preference
            (b) = int(input("What is the second number you'd like to use? ")) # sets value of 2nd number per user preference
            if (choice).lower() == 'add':
                result = a + b
                print (f' {a} plus {b} = {result}.')
            elif (choice).lower() == 'subtract':
                result = a - b
                print (f' {a} minus {b} = {result}.')
            elif (choice).lower() == 'multiply':
                result = a * b
                print (f' {a} times {b} = {result}.')
            elif (choice).lower() == 'divide':
                result = a / b
                print (f' {a} divided by {b} = {result}.')

math_choice()




# Create pyramid
def create_pyramid(n):
    x = "x"                             # sets value of x variable to 'x'
    column = n - 1                      # sets value which will determine empty spaces before x row
    for i in range(1, n*2, 2):          # sets range to all odd numbers up to 2n
        empty_space = column * " "      # defines quantity of empty spaces to start each x row
        final = (empty_space + (x*i))   # creates each row
        print (final)                   # prints each row
        column -= 1                     # empty space at start of subsequent row by 1 
 
create_pyramid(14)





