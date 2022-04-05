# functions go here

# checks input is a number more that zero
def num_check(question):
        valid = False
        while not valid:

            error = "please enter a number that is more that zero"

            try:

                # ask user to enter a number
                response = float(input(question))

                # check number more than zero
                if response > 0:
                    return response

                # outputs error if input is iinvalid
                else:           
                    print(error)
                    print()

            except ValueError:
                print(error)
    

  
# Main Routine goes here

keep_going=""
while keep_going=="":

    width = num_check("width:  ")
    height = num_check("height: ")

    # calculate area (width x height)
    area = width * height

    # calu;ate perimeter (width + height) x 2
    perimter = 2 * (width + height)

    # Output area and perimeter 
    print("permeter: {} units".format(perimter))
    print("Area: {} square units".format(area))


    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")
