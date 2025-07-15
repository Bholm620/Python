# Python
# Brandon Holm
# Nice or Mean 
# Game

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player for
        playing again and continue with the game
    """
# meaning, if we do not already have this user's name,
# then they are a new player, and we need to get her name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick =="n":
            print("The stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \n menacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the three variables to the score()



def show_score(nice,mean,name):
    print("\n{}, your current total: \n ({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else: nice_mean(nice,mean,name)

def win(nice,mean,name):
    #substitute the () wildcards with our own variable values
    print("\nNice job {}, you win! \nEveryone loves you and nothing hurts!".format(name))
    #call again function to pass in our variable
    again(nice,mean,name)


def lose(nice,mean,name):
    #substitute the () wildcards with our own variable values
    print("\nTerrible job {}, you deead! \nEveryone hates you and everything hurts!".format(name))
    #call again function to pass in our variable
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("See ya later!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', ( N ) for 'No':\n>>>")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    #nortice we do not repeat the same variable
    start(nice,mean,name)






























    

if __name__ == "__main__":
    start()
