import turtle
import pandas


def add_state_to_map(state, x, y):
    t = [turtle.Turtle()]
    t[-1].penup()
    t[-1].hideturtle()
    t[-1].goto(x=x, y=y)
    t[-1].write(arg=state, align="Center", font=('Courier', 8, "normal"))


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []
game_is_on = True
while game_is_on:
    # Prompts the user for the answer_state and tracks the score
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # If the state is safe to add and hasn't been guessed before then place the state on the map and update the guessed_states
    if (answer_state in list(data.state)) and (answer_state not in guessed_states):
        x, y = int(data[data.state == answer_state].x), int(data[data.state == answer_state].y)
        add_state_to_map(answer_state, x, y)
        guessed_states.append(answer_state)

    # Exit the game
    if len(guessed_states) >= 50 or answer_state == "Exit":
        game_is_on = False

# Print out all states not guessed by the user
missing_states = [state for state in data.state.to_list() if state not in guessed_states]
df = pandas.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")
