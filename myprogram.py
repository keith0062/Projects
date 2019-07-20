
the_matrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

professions = ["","","",""]
adj = ["",""]

print("Welcome user.")
print("Let's play a game of madlibs.")
neo = input("Please share with me your name.\n")
print(f"Hello, {neo}. Are you ready?")
the_matrix = input("What is something you want to know more about? ")
print(f"Ooh! you want to know more about {the_matrix}, huh?")
print(f"Okay, well tell me what you already know about {the_matrix}.")
system = input(f"What noun would you categorize {the_matrix} as? ")


story = (f"{the_matrix} is a {system}, {neo}. That {system} is our {enemy}. " +
f"But when you're {inside}, you look around, what do you see? " +
f"{professions[0]}, {professions[1]}, {professions[2]}, {professions[2]}. The very minds " +
f"of the people we are trying to {save}. But until we do, " +
f"these people are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these people " +
f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

print(story)