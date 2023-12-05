from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minute =  math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        window.after(1000, count_down, count -1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

# Canvas setup w/ tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# start button configuratioons
start_button = Button(text="Start", highlightthickness=0, borderwidth=0)
start_button.grid(column=0, row=3)

# command to trigger countdown on start button press
start_button.config(command=start_timer) 

# reset button configurations
reset_button = Button(text="Reset", highlightthickness=0, borderwidth=0)
reset_button.grid(column=2, row=3)

check_mark = Label(text="✅", fg=GREEN, highlightthickness=0, bg=YELLOW)
check_mark.grid(column=1, row=5)




window.mainloop()

