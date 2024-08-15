from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    global REP
    window.after_cancel(timer)
    REP = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REP
    REP += 1

    if REP % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        counter(LONG_BREAK_MIN * 60)
    elif REP % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        counter(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        counter(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global REP
    minute = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minute:02}:{seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)
    else:
        if REP % 2 == 0:
            checkmark_label.config(text="✔" * (REP // 2))
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
