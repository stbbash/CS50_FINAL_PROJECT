import sys
import emoji
from pyfiglet import Figlet
from models import boys, girls, user, user_age, user_name, user_height, user_build, user_shape, user_sex, user_complexion, user_password
from views import check_user_input, check_name, check_database

""" FUNCTION TO CHECK USERS AGE """
def check_age():
    global user_age
    while True:
        try:
            age_str = input(emoji.emojize("HOW OLD ARE YOU? :face_savoring_food: ", language='alias')).strip()
            if age_str.lower() == "q":
                sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))
            age = int(age_str)
            if age < 18:
                sys.exit(emoji.emojize("Too YOUNG to Register, age should be between 18 - 85 :underage: ", language='alias'))
            if age > 80:
                sys.exit(emoji.emojize("Too OLD to Register, age should be between 18 - 85 :smiling_face_with_tear: ", language='alias'))
            else:
                user_age = age
                print(emoji.emojize("You are Eligible to Register :beaming_face_with_smiling_eyes: ", language='alias'))
                return user_age
        except ValueError:
            print(emoji.emojize("Please enter a valid age as a number or type 'q' to quit program :anxious_face_with_sweat: ", language='alias'))
        except KeyboardInterrupt:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))
        except EOFError:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))

""" FUNCTION TO CHECK IF USER HAS REGISTERED """
def check_register_and_login():
    global user_sex
    global user_name
    while True:
        try:
            name = input(emoji.emojize("Insert Username :open_book:: ", language='alias')).strip().capitalize()
            if not name:
                print(emoji.emojize("Must be Registered to Continue Type 'b' to go back and Register or 'q' to quit program :smiling_face_with_tear:", language='alias'))
            elif name in boys or name in girls:
                user_name = name
                break
            elif name.lower() == "q":
                sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))
            elif name.lower() == "b":
                return "back"
            else:
                print(emoji.emojize("Username not found :underage: Type 'b' to go back and Register or 'q' to quit program :smiling_face_with_tear:", language='alias'))
        except KeyboardInterrupt:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))
        except EOFError:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))
    while True:
        try:
            password = input(emoji.emojize("Insert Password :open_book:: ", language='alias'))
            if not password:
                print(emoji.emojize("Please Insert Password else Type 'b' to go back and Register or 'q' to quit program :smiling_face_with_tear:", language='alias'))
            elif user_name in boys and password in boys[user_name]:
                user_sex = "boy"
                print(Figlet(font='doom', width=200).renderText(f"Welcome Back {user_name}"))
                print(emoji.emojize(f"You are Logged in as {user_name.capitalize()} :boy: ", language='alias'))
                print(emoji.emojize("You can choose a Girl from Our List :face_exhaling: ", language='alias'))
                return user_sex
            elif user_name in girls and password in girls[user_name]:
                user_sex = "girl"
                print(Figlet(font='doom', width=200).renderText(f"Welcome Back {user_name}"))
                print(emoji.emojize(f"You are Logged in as {user_name.capitalize()} :girl: ", language='alias'))
                print(emoji.emojize("You can choose a Boy from Our List :face_exhaling: ", language='alias'))
                return user_sex
            elif password.lower() == "q":
                sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))
            elif password.lower() == "b":
                return "back"
            else:
                print(emoji.emojize("Password not correct :underage: Type 'b' to go back and Register or 'q' to quit program :smiling_face_with_tear:", language='alias'))
        except KeyboardInterrupt:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))
        except EOFError:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))



def register(age):
    global user
    global user_name
    global user_sex
    global user_build
    global user_height
    global user_shape
    global user_password
    global user_complexion
    if age:
        """ GET THE USERS DETAILS AND ADD USERS DETAILS TO DATABASE"""
        while True:
            try:
                name = input(emoji.emojize("Enter Username: :identification_card:  ")).strip().lower()
                if name.lower() == "q":
                    sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))
                if name.capitalize() in boys or name.capitalize() in girls:
                    print(emoji.emojize("Username is already taken. Please choose another :anxious_face_with_sweat:", language='alias'))
                elif check_name(name):
                    user_name = name
                    break
                else:
                    print(emoji.emojize("Please enter a valid username or type 'q' to quit program :anxious_face_with_sweat: ",language='alias'))
            except ValueError:
                print(emoji.emojize("Please enter a valid username or type 'q' to quit program :anxious_face_with_sweat: ",language='alias'))
            except KeyboardInterrupt:
                sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))
            except EOFError:
                sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))
        user_sex = check_user_input("Boy or Girl: ", ["boy", "girl"])
        if user_sex == "boy":
            print(emoji.emojize(f"You Registered as a {user_sex.capitalize()} :boy: ", language='alias'))
            user_build = check_user_input("Athletic or Non-athletic: ", ["athletic", "non-athletic"])
            user_height = check_user_input("Tall or Short: ", ["tall", "short"])
            user_shape = check_user_input("Muscular or Slim: ", ["muscular", "slim"])
            user_complexion = check_user_input("Fair or Dark: ", ["fair", "dark"])
            user_password = input("Insert a password: ").strip().lower()
            user = [age, user_build, user_height, user_shape, user_complexion, user_password]
            boys[user_name.capitalize()] = user
            print(Figlet(font='doom', width=200).renderText("Thanks for Registering "))
            print(emoji.emojize("You can choose a Girl from Our List :face_exhaling: ", language='alias'))

        elif user_sex == "girl":
            print(emoji.emojize(f"You Registered as a {user_sex.capitalize()} :girl: ", language='alias'))
            user_build = check_user_input("Athletic or Non-athletic: ", ["athletic", "non-athletic"])
            user_height = check_user_input("Tall or Short: ", ["tall", "short"])
            user_shape = check_user_input("Curvy or Slim: ", ["curvy", "slim"])
            user_complexion = check_user_input("Fair or Dark: ", ["fair", "dark"])
            user_password = input("Insert a password: ")
            user = [age, user_build, user_height, user_shape, user_complexion, user_password]
            girls[user_name.capitalize()] = user
            print(Figlet(font='doom', width=200).renderText("Thanks for Registering "))
            print(emoji.emojize("You can choose a Boy from Our List :face_exhaling: ", language='alias'))
    return user_sex