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
timer = None
check = ["", "", "✔", "", "✔✔", "", "✔✔✔", "", "✔✔✔✔"]
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_mark.config(text=check[reps])

# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
def start_timer():
    global reps
    global check
    reps += 1
    if reps % 8 == 0:
        check_mark.config(text=check[reps])
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        check_mark.config(text=check[reps])
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)








# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_minutes = count // 60
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
tomato_image = PhotoImage(file="/Users/pietertasseron/Documents/PycharmProjects/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50))

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark.grid(column=1, row=3)










window.mainloop()
