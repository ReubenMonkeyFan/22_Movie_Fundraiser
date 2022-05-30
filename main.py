# functions here
def not_blank(question, error):
    valid = False
    while not valid:

        response = str(input(question))

        while response != "":
            return response
        else:
            print(error)


# main code

name = not_blank("What is your name? ", "This can't be blank, please enter your name")
