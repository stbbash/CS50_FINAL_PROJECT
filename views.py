import sys
import emoji
import re
import inflect


""" FUNCTION FOR CHECKING DATABASE """
def check_database(data_base: dict, data: list):
    chosen_ones = []
    for person, preferences in data_base.items():
        if all(preference in preferences for preference in data):
            chosen_ones.append(person)
    return chosen_ones


""" FUNCTION FOR CHECKING USERS INPUT """
def check_user_input(arg2: str, arg3: list):
    while True:
        try:
            user_input = input(f"{arg2} ").lower().strip()
            if user_input == "q":
                sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear: ", language='alias'))
            if user_input in arg3:
                return user_input
            else:
                print(emoji.emojize("Enter an option from the list or type 'q' to quit program :man_facepalming_medium_skin_tone: ", language='alias'))
        except ValueError:
            print(emoji.emojize("Enter an option from the list or type 'q' to quit program :man_facepalming_medium_skin_tone: ", language='alias'))
        except KeyboardInterrupt:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))
        except EOFError:
            sys.exit(emoji.emojize("Thanks for your time :smiling_face_with_tear:", language='alias'))


""" FUNCTION TO CHECK VALIDITY OF USERS NAME """
# CHECK FOR LENGTH OF STRING AND STRING ONLY CONTAINS ALPHABETS
def check_name(name: str):
    if 2 < len(name) < 15 and re.search(r"([a-z])", name, re.IGNORECASE):
        return True
    return False


""" CLASS TO CHOoSE THE PERSON """
class Person:
    def __init__(self):
        self.person = None

    def choose(self, persons):
        if persons == []:
            return emoji.emojize("Your Type of Person is not Available :expressionless_face:", language='alias')
        elif len(persons) < 2:
            person = persons[0]
            print(emoji.emojize(f"{person.capitalize()} is Available :winking_face_with_tongue:", language='alias'))
            decide = input(f"Do you want to choose {person.capitalize()} 'Yes' or 'No' :").lower().strip()
            if decide == 'yes':
                return emoji.emojize(f"You Choose {person.capitalize()} :winking_face_with_tongue:", language='alias')
            else:
                return emoji.emojize("Your Type of Person is not Available :expressionless_face:", language='alias')
        else:
            persons_str = ', '.join([person.lower() for person in persons])
            persons_list = [person.lower() for person in persons]
            p = inflect.engine()
            mylist = p.join(persons)
            print(emoji.emojize(f"The following people {mylist} are Available, So Pick One Person From The List :grinning_face_with_big_eyes: ", language='alias'))
            decide = check_user_input(persons_str, persons_list)
            return emoji.emojize(f"You Choose {decide.capitalize()} :winking_face_with_tongue:", language='alias')

    def __str__(self):
        return self.choose(self.person)
