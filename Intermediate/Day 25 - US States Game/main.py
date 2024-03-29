import turtle

import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"({len(guessed_states)}/50) Guess the state", prompt="Guess a state name!")
    if answer_state.title() == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state.title() in all_states:
        guessed_states.append(answer_state)
        point = turtle.Turtle()
        point.hideturtle()
        point.penup()
        state_data = data[data["state"] == answer_state]
        point.goto(int(state_data["x"]), int(state_data["y"]))
        point.write(state_data["state"].item())

# def get_mouse_click_coord(x, y):
#    print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()
