"""
This class lets you automate the creation of a single letter to many letters from a list of recipients
"""

PATH_TO_LETTER = "./Input/Letters/starting_letter.txt"
PATH_TO_NAMES = "./Input/Names/invited_names.txt"
PATH_TO_DESTINATION = "./Output/ReadyToSend/"

class Mail_Merge:
    def __init__(self):
        self.names = self.get_names()

    def get_names(self):
        list_of_names = []
        with open(PATH_TO_NAMES) as names:
            for line in names.readlines():
                list_of_names.append(line.strip())
        return list_of_names

    def get_letter(self):
        with open(PATH_TO_LETTER) as file:
            letter = file.read()
        return letter

    # Requires the name of the recipient to whom you are sending the mail to
    def create_letter(self, name):
        with open(PATH_TO_DESTINATION + f"letter_for_{name}.txt", mode="w") as new_letter:
            new_letter.write(self.get_letter().replace("[name]", name))