import tkinter as tk
import random
import time

start_time = time.time()
results_list = list()
wrong_clicks = 0
total_clicks = 0

window = tk.Tk()
window.geometry("300x300")
window.title("Check your reaction")
label = tk.Label(
        text="Let's play",
        font=("Arial", 15),
        foreground="black",
        background="gray",
        width=100,
        height=3
)


def start_game():
    for c in window.children:
        window.children[c].pack()
    reset_btn.pack(side="bottom")  # just example how to move to the bottom
    greeting.pack_forget()
    start_button.pack_forget()
    window.after(2000, color_update)


greeting = tk.Label(
        text="Press 'Start' to launch",
        font=("Arial", 15),
        foreground="black",
        background="orange",
        width=100,
        height=3
)
start_button = tk.Button(
        text="Start",
        font=("Arial", 12),
        bg="red",
        fg="black",
        width=10,
        height=1,
        command=start_game
)
greeting.pack()
start_button.pack(pady=10)

frame = tk.Frame(
        height=10
)


def wrong_clicks_counter():
    global wrong_clicks, total_clicks
    total_clicks += 1
    if label.config("text")[-1] != "red":
        wrong_clicks += 1
    result_wrong_click.config(
            text=f"False clicks: {wrong_clicks} from {total_clicks}")  # display
    # false clicks


def time_counter():
    if label["background"] == "red":
        run_time = round(time.time() - start_time, 2)
        results_list.append(run_time)
        average_time = round(sum(results_list) / len(results_list), 2)
        result.config(text=f"Time: {run_time}s")  # display result
        result_average.config(
                text=f"Average time: {average_time}s")  # display average result


def button_state_switcher(val):  # This function allows us to lock the button,
    # but it allows user to click many timee on button
    # and not receive "false clicks" and receive "short" reaction to thr "RED"
    if val != button["state"]:  # was good but reding is complicated
        if val == "disabled":
            button.config(state=val, bg="gray80")
        elif val == "normal":
            button.config(state=val, bg="orange")


def show_result():
    time_counter()
    wrong_clicks_counter()
    button_state_switcher("disabled")


button = tk.Button(
        text="Click me if RED !",
        font=("Arial", 12),
        bg="orange",
        fg="black",
        width=12,
        height=2,
        command=show_result  # this action is little overloaded but it's ok
)

result = tk.Label(
        text="Time: 0.0s",
        foreground="green",
        font=("Arial", 15)
)

result_average = tk.Label(
        text="Average time: 0.0s",
        foreground="green",
        font=("Arial", 15)
)

result_wrong_click = tk.Label(
        text="False clicks: 0 from 0",
        foreground="red",
        font=("Arial", 15)
)


def clear_data():
    global wrong_clicks, total_clicks
    wrong_clicks = 0
    total_clicks = 0
    results_list.clear()
    result.config(text=f"Time: 0.0s")
    result_average.config(text=f"Average time: 0.0s")
    result_wrong_click.config(
            text=f"False clicks: {wrong_clicks} from {total_clicks}")


reset_btn = tk.Button(
        text="Reset",
        font=("Arial", 12),
        fg="black",
        width=10,
        height=1,
        command=clear_data
)


def color_update():
    colors = ["red", "green", "yellow", "blue"]
    title_color = colors[random.randint(0, len(colors) - 1)]
    random_time = random.randint(1000, 3000)
    label.config(background=title_color, text=title_color)
    button_state_switcher("normal")
    label.after(random_time - 300,
                lambda: label.config(background="gray", text=""))

    if label.config("text")[-1] == "red":  # the same as above
        # label["background"] easier to read
        global start_time
        start_time = time.time()
    window.after(random_time, color_update)


window.mainloop()

