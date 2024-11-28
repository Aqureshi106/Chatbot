import string

data = {  # example
    "courses": {
        "CS101": {"time": "10:00 AM", "classroom": "Room 101"},
        "MATH102": {"time": "12:00 PM", "classroom": "Room 202"},
    },
    "professors": {"Smith": {"office": "Room 301", "hours": "2:00 PM - 4:00 PM"}},
    "library": {
        "hours": "8:00 AM - 8:00 PM",
        "rules": "Books can be borrowed for 2 weeks.",
    },
}


def greeting_handler(query: str) -> str:
    greetings = ["hello", "salutations", "greetings", "hi", "hey", "what's up"]
    if any(greet in query.lower() for greet in greetings):
        return "Greetings; how can I be of assistance?"


def find_course(name: list) -> str:
    if any(check in name for check in data["courses"]):
        for i in data["courses"]:
            if i in name:
                course = data["courses"][i.upper()]
                return "{0} is at {1} in {2}.".format(
                    i.upper(), course["time"], course["classroom"]
                )
    else:
        return unclear()


def find_prof(name: list) -> str:
    name = [word.lower() for word in name]
    name = [word.capitalize() for word in name]
    if any(check in name for check in data["professors"]):
        for i in data["professors"]:
            if i in name:
                prof = data["professors"][i]
                return "Prof.{0}'s office is at {1} with hours {2}.".format(
                    i, prof["office"], prof["hours"]
                )
    else:
        return unclear()


def fix(text: str) -> list:
    l = text.split()
    l = [word.replace("'s", "") for word in l]
    l = [word.upper() for word in l]
    translator = str.maketrans("", "", string.punctuation)
    l = [word.translate(translator) for word in l]
    return l


def unclear() -> str:
    return "My apologies, I didn't understand; may you rephrase?"


def process(query: str) -> str:
    if "course" in query.lower():
        course = fix(query)
        return find_course(course)
    elif "library" in query.lower():
        return "Library hours are {0}. {1}".format(
            data["library"]["hours"], data["library"]["rules"]
        )
    elif "professor" in query.lower():
        prof_name = fix(query)
        return find_prof(prof_name)
    greeting = greeting_handler(query)
    if greeting:
        return greeting
    return unclear()


while True:
    response = input("You: ")
    print("Chatbot:",process(response))