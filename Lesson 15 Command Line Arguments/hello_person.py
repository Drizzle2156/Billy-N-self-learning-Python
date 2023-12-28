# add this new stuff
# this function creates a dictionary, and upon inputting a name and 1 of the 3 languages it will print the msg with inputs
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


# REMEMBER -> used to determine if a Python script is being run as the main program or if it is being imported as a module into another script. It only applies to the code block line 13-26
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument("-n", "--name", metavar="name", required=True,  help="The name of the person to greet."
                        )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()
    hello(args.name, args.lang)
    # msg = f"Hello {args.name}!"
    # print(msg)
# can't run this python file, have to pass an argument in terminal
# in terminal typed in
# python3 hello_person.py
# python3 hello_person.py -h -> contents from parser
# python3 hello_person.py -n -> Hello Dave!
# then added the new stuff at line 1


# at 5:10:00 enter more command lines
# python3 hello_person.py -n "Dave" -l "French" -> get error, and invalid choice
# python3 hello_person.py -n "Dave" -l "German" -> Hallo Dave!
