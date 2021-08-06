import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="What's another state")
    answer_state_final = answer_state.title()

    if answer_state == "exit":
        remaining_states = []
        for state in all_states:
            if state not in guessed_states:
                remaining_states.append(state)
        print(remaining_states)
        # rem_data = pandas.DataFrame(remaining_states)
        # rem_data.to_csv("learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state_final)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state_final)

screen.exitonclick()
