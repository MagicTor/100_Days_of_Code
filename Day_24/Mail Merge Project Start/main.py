list_of_names = []
with open("./Input/Names/invited_names.txt") as names:
    for line in names.readlines():
        list_of_names.append(line.strip())


def create_letter(name):  # create a file called letter_for_{name}.txt
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        with open("./Input/Letters/starting_letter.txt") as letter:
            first_line = letter.readline().replace("[name]", name)
            new_letter.write(first_line)

            for lines in letter.readlines():
                new_letter.write(lines)


for name in list_of_names:
    create_letter(name)
