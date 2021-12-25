import tkinter as tk
import random
import time

start_time = time.time()
results_list = []

window = tk.Tk()
window.geometry("300x300")
window.title("Check your reaction")
label = tk.Label(
    text="Timer Calculator",
    font=("Arial", 15),
    foreground="black",  # Set the text color to black
    background="gray",  # Set the background color to gray
    width=100,
    height=2
)

frame = tk.Frame(
    height=10
)


def send_message():
    run_time = round(time.time() - start_time, 2)
    results_list.append(run_time)
    average_time = round(sum(results_list) / len(results_list), 2)
    result.config(text=f"Time: {run_time}")
    result_average.config(text=f"Average time: {average_time}")


button = tk.Button(
    text="Click me!",
    font=("Arial", 12),
    bg="orange",
    fg="black",
    width=10,
    height=1,
    command=send_message
)

result = tk.Label(
    text="Time: 0.0",
    foreground="red",  # Set the text color to red
    font=("Arial", 15)
)

result_average = tk.Label(
    text="Average time: 0.0",
    foreground="red",  # Set the text color to red
    font=("Arial", 15)
)

frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)

for c in window.children:
    print(c)
    window.children[c].pack()


def timer_update():
    colors = ["red", "green", "blue", "yellow"]
    value = random.randint(0, len(colors) - 1)
    label.config(background=colors[value], text=colors[value])
    window.after(2000, timer_update)
    if label.config("background")[-1] == "red":
        global start_time
        start_time = time.time()


window.after(2000, timer_update)

window.mainloop()
