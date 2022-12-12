import character_class

def new_game():
    char_name = input("Greetings adventurer, you are the last hope of the kingdom of Yggdra. Could you please tell me your name?\n")
    print("The Kingdon of Yggdra is very thankful to have a brave adventurer like you, " + char_name)

    return character_class.Character(char_name)


character = new_game()

print(character.health)