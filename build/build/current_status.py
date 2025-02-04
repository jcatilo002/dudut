from tkinter import Tk, Canvas, Button, Label
from datetime import datetime, timedelta
import data_storage

def open_current_status_tab():
    current_status_tab = Tk()
    current_status_tab.geometry("393x852")
    current_status_tab.configure(bg="#4E7DBB")
    current_status_tab.title("Current Status")

    canvas = Canvas(
        current_status_tab,
        bg="#4E7DBB",
        height=852,
        width=393,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    def show_details(date):
        water_intake = data_storage.data_storage["water_intake"].get(date, "No data")
        steps = data_storage.data_storage["steps"].get(date, "No data")
        exercise_data = data_storage.data_storage["exercise"].get(date, {})
        exercise = exercise_data.get("exercise", "No data")
        duration = exercise_data.get("duration", "No data")
        repetitions = exercise_data.get("repetitions", "No data")
        sets = exercise_data.get("sets", "No data")
        details_label.config(text=f"Date: {date}\nWater Intake: {water_intake} ml\nSteps: {steps}\nExercise: {exercise}\nDuration: {duration} minutes\nRepetitions: {repetitions}\nSets: {sets}")

    def create_calendar(month_offset=0):
        for widget in current_status_tab.winfo_children():
            if isinstance(widget, Button) and widget != prev_button and widget != next_button:
                widget.destroy()

        today = datetime.now()
        target_month = (today.replace(day=1) + timedelta(days=month_offset * 30)).replace(day=1)
        while target_month.month != (today.month + month_offset - 1) % 12 + 1:
            target_month -= timedelta(days=1)
        next_month = (target_month.replace(day=28) + timedelta(days=4)).replace(day=1)
        days_in_month = (next_month - timedelta(days=1)).day

        x, y = 20, 100
        for day in range(1, days_in_month + 1):
            is_today = day == today.day and month_offset == 0 and today.month == target_month.month
            day_button = Button(
                current_status_tab,
                text=str(day),
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                bg="#FFD700" if is_today else "#D9D9D9",
                command=lambda d=day: show_details(f"{target_month.strftime('%Y-%m')}-{d:02d}")
            )
            day_button.place(x=x, y=y, width=30, height=30)
            x += 40
            if x > 360:
                x = 20
                y += 40

        canvas.itemconfig(month_label, text=target_month.strftime("%B %Y"))

    def prev_month():
        nonlocal month_offset
        month_offset -= 1
        create_calendar(month_offset)

    def next_month():
        nonlocal month_offset
        month_offset += 1
        create_calendar(month_offset)

    month_offset = 0

    month_label = canvas.create_text(
        196.0,
        50.0,
        text="",
        fill="#FFFFFF",
        font=("Arial-BoldMT", 24)
    )

    prev_button = Button(
        current_status_tab,
        text="<",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=prev_month,
        bg="#FFD700",
        fg="#000000",
        font=("Arial-BoldMT", 14)
    )
    prev_button.place(x=20, y=40, width=30, height=30)

    next_button = Button(
        current_status_tab,
        text=">",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=next_month,
        bg="#FFD700",
        fg="#000000",
        font=("Arial-BoldMT", 14)
    )
    next_button.place(x=340, y=40, width=30, height=30)

    details_label = Label(
        current_status_tab,
        text="",
        bg="#4E7DBB",
        fg="#FFFFFF",
        font=("Arial-BoldMT", 16)
    )
    details_label.place(x=20, y=400)

    create_calendar()
    current_status_tab.mainloop()

if __name__ == "__main__":
    open_current_status_tab()
