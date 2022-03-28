# check that users enter a number that is more that zero
valid = False
while not valid:

    # ask user to enter a number
    response = float(input("Enter a number: "))

    # check number more than zero
    if response > 0:
        valid = True

    # outputs error if input is iinvalid
    else:           
        print("Please enter a number that is more than zero")
        print()



