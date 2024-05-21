from views import check_database, check_user_input

""" Fake DataBase Description
Height      -> Text field(max=255, min=1)
Shape       -> Text field(max=255, min=1)
Complexion  -> Text field(max=255, min=1)
password     -> Text field(max=255, min=1)
build     -> Text field(max=255, min=1)
age         -> Integer field
"""

# Fake DataBase for Girls
girls = {
    "Precious": [19, "non-athletic", "short", "slim", "dark", "12345precious"],
    "Helen": [24, "athletic", "tall", "curvy", "dark", "12345helen"],
    "Amaka": [29, "athletic", "short", "curvy", "fair", "12345amaka"],
    "Jenny": [22, "non-athletic", "tall", "curvy", "dark", "12345deborah"],
    "Daby": [22, "athletic", "tall", "curvy", "dark", "12345daby"],
    "Steph": [27, "non-athletic", "short", "slim", "dark", "12345steph"],
    "Monica": [24, "athletic", "short", "curvy", "dark", "12345monica"]
}

# Fake DataBase for Boys
boys = {
    "Bash": [30, "athletic", "tall", "slim", "fair", "12345bash"],
    "Donatus": [30, "athletic", "tall", "slim", "fair", "12345donatus"],
    "Ajaezu": [30, "athletic", "tall", "slim", "fair", "12345"],
    "Buchi": [31, "athletic", "tall", "muscular", "fair", "12345buchi"],
    "Tony": [32, "athletic", "short", "muscular", "dark", "12345tony"],
    "Bukky": [33, "athletic", "short", "muscular", "dark", "12345bukky"],
    "Paul": [30, "non-athletic", "tall", "slim", "dark", "12345paul"]
}

""" Users default details before inserting into our fake database """
user = []
user_sex = None
user_name = None
user_age = None
user_build = None
user_height = None
user_shape = None
user_complexion = None
user_password = None

def get_boy_or_girl(sex):
    if sex == "boy":
        build = check_user_input("Athletic or Non-athletic: ", ["athletic", "non-athletic"])
        height = check_user_input("Tall or Short: ", ["tall", "short"])
        shape = check_user_input("Curvy or Slim: ", ["curvy", "slim"])
        complexion = check_user_input("Fair or Dark: ", ["fair", "dark"])
        chosen_girl = [build, height, shape, complexion]
        return check_database(girls, chosen_girl)
    elif sex == "girl":
        build = check_user_input("Athletic or Non-athletic: ", ["athletic", "non-athletic"])
        height = check_user_input("Tall or Short: ", ["tall", "short"])
        shape = check_user_input("Muscular or Slim: ", ["muscular", "slim"])
        complexion = check_user_input("Fair or Dark: ", ["fair", "dark"])
        chosen_boy = [build, height, shape, complexion]
        return check_database(boys, chosen_boy)
