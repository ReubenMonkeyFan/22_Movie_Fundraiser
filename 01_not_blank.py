 # function here
def not_blank(question):
    valid = False
    while not valid:

        response = str(input(question))

        if response == "" or response == " ":
            print("You need to enter a name! ")
        else:
            return response

# main code

not_blank("What is your name? ")
