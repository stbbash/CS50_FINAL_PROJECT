import pyttsx3
import emoji
import sys
from pyfiglet import Figlet
from registration import check_register_and_login, register, check_age, user_age, user_sex
from views import check_user_input, check_database, Person
from models import get_boy_or_girl, boys, girls


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "run":
        print(Figlet(font='cyberlarge', width=200).renderText("Hello, World"))
        print(emoji.emojize("WELCOME TO BASH DATING SITE :smiling_face_with_sunglasses:", language='alias'))
        global user_sex
        option = check_user_input("Login or Register: ", ["login", "register"])
        if option == "register":
            welcome_verification()
            choose_and_render_person()
        else:
            user_sex = check_register_and_login()
            if user_sex ==  "back":
                main()
            else:
                choose_and_render_person()
    elif len(sys.argv) == 2 and sys.argv[1] == ".desc":
        admin()
    elif len(sys.argv) == 2 and sys.argv[1] == ".schema":
        schema()
    else:
        sys.exit("Invalid input")



""" WELCOME AND VERICATION FUNCTION"""
def welcome_verification():
    global user_age, user_sex
    user_age = check_age()
    user_sex = register(user_age)
    return user_sex


""" FUNCTION TO GET USERS FROM THE LIST AND CHOOSE AVAILABLE USERS """
def choose_and_render_person():
    global user_sex
    lucky_one = Person().choose(get_boy_or_girl(user_sex))
    print(Figlet(font='cyberlarge').renderText("Available Person: "))
    print(lucky_one)
    engine = pyttsx3.init()
    engine.say(lucky_one)
    engine.runAndWait()
    choose_again()

""" FUNCTION TO PROMPT THE USER TO CHOOSE AGAIN """
def choose_again():
    print(emoji.emojize("Do you want to choose again :face_exhaling: ", language='alias'))
    answer = check_user_input("Yes or no: ", ["yes", "no"])
    if answer == "yes":
        choose_and_render_person()
    else:
        sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))

"""Run administrative tasks."""
def admin():
    with open('README.md', 'r') as file:
        result = file.read()
        print(Figlet(font='small').renderText("DESCRIPTION"))
        print(result)
    return 0
def schema():
    print(Figlet(font='small').renderText("BOYS DATABASE"))
    print(boys)
    print(Figlet(font='small').renderText("GIRLS DATABASE"))
    print(girls)
    return 0
if __name__ == "__main__":
    main()
