import tkinter as tk
import json
from datetime import date, datetime
import random
import time

start_time = time.time()
results_list = list()
average_time = 0
success = 0
wrong_clicks = 0
total_clicks = 0
player = ""

window = tk.Tk()
window.geometry("400x400")
window.resizable(width=False, height=False)
window.title("Check your reaction")
title = tk.Label(
    text="Press the button if it's RED!",
    font=("Arial", 15),
    foreground="black",
    background="gray80",
    width=100,
    height=3
)

label_entry = tk.Label(
    font=("Arial", 12),
    text="Input your name:"
)

entry = tk.Entry(
    font=("Arial", 15),
    justify="center"
)

err = tk.Label(text="", foreground="red")
err.pack()


def start_game(*event):
    name = entry.get()
    if name.isalpha() and len(name) >= 2:
        global player
        player = name
        for c in window.children:
            window.children[c].pack()
        button.pack(pady=10)
        save_button.pack(side="bottom", pady=10)
        for i in [greeting, start_button, label_entry, entry, err]:
            i.pack_forget()
        window.after(2000, color_update)
    else:
        err.config(text="The name cannot be empty and must contain\n two letters at least.")


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
label_entry.pack(pady=10)
entry.pack()
entry.bind("<Key-Return>", start_game)
err = tk.Label(text="", foreground="red", height=2)
err.pack()
start_button.pack()


def clicks_counter():
    global wrong_clicks, total_clicks
    total_clicks += 1
    if button["background"] != "red":
        wrong_clicks += 1
    result_wrong_click.config(
        text=f"False clicks: {wrong_clicks} from {total_clicks}")
    success_counter()


def success_counter():
    global success
    try:
        success = 100 - int(wrong_clicks / total_clicks * 100)
        if success >= 50:
            save_button.configure(state="normal")
        else:
            save_button.configure(state="disabled")
    except ZeroDivisionError:
        success = 0
        save_button.configure(state="disabled")


def time_counter():
    global average_time
    if button["background"] == "red":
        run_time = round(time.time() - start_time, 2)
        results_list.append(run_time)
        average_time = round(sum(results_list) / len(results_list), 2)
        result.config(text=f"Time: {run_time}s")  # display result
        result_average.config(
            text=f"Average time: {average_time}s")  # display average result


def button_state_switcher(btn, val):
    if val != btn["state"]:
        if val == "disabled":
            btn.config(state=val, bg="gray80")
        elif val == "normal":
            btn.config(state=val)


def show_result():
    time_counter()
    clicks_counter()
    button_state_switcher(button, "disabled")


button = tk.Button(
    text="Click me!",
    font=("Arial", 12),
    bg="orange",
    fg="black",
    width=20,
    height=4,
    border=5,
    command=show_result
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
    success_counter()
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


def save_data():
    today = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    if success >= 50:
        try:
            with open("results.json", "r") as f:
                data = json.load(f)
                if "id_" + player in data:
                    with open("results.json", "w") as f:
                        data["id_" + player][today] = {"best_result": min(results_list),
                                                       "average_result": average_time}
                        json.dump(data, f)
                        print("Updated")
                else:
                    with open("results.json", "w") as f:
                        data["id_" + player] = {
                            "name": player,
                            today: {
                                "best_result": min(results_list),
                                "average_result": average_time
                            }
                        }
                        json.dump(data, f)
                        print("New user added")

        except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
            with open("results.json", "w") as f:
                data = {"id_" + player: {
                    "name": player,
                    today: {
                        "best_result": min(results_list),
                        "average_result": average_time
                    }
                }
                }
                json.dump(data, f)
                print("New file created")


save_button = tk.Button(
    text="Save result",
    font=("Arial", 12),
    fg="black",
    width=10,
    height=1,
    state="disabled",
    command=save_data
)


def color_update():
    colors = ["red", "green", "blue"]
    button_color = colors[random.randint(0, len(colors) - 1)]
    random_time = random.randint(1000, 3000)
    button_state_switcher(button, "normal")
    button.config(background=button_color)
    button.after(random_time - 300,
                 lambda: button.config(background="gray80"))

    if button["background"] == "red":
        global start_time
        start_time = time.time()
    window.after(random_time, color_update)


window.mainloop()
