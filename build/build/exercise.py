from tkinter import Tk, Canvas, Entry, Button, Label
import data_storage

def open_exercise_tab():
    exercise_tab = Tk()
    exercise_tab.geometry("393x852")
    exercise_tab.configure(bg="#4E7DBB")
    exercise_tab.title("Exercise")

    canvas = Canvas(
        exercise_tab,
        bg="#4E7DBB",
        height=852,
        width=393,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    Label(exercise_tab, text="Date (YYYY-MM-DD):", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=50)
    date_entry = Entry(exercise_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    date_entry.place(x=250, y=50, width=100, height=30)

    Label(exercise_tab, text="Exercise:", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=100)
    exercise_entry = Entry(exercise_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    exercise_entry.place(x=250, y=100, width=100, height=30)

    Label(exercise_tab, text="Duration (minutes):", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=10, y=150)
    duration_entry = Entry(exercise_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    duration_entry.insert(0, "optional")
    duration_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, duration_entry))
    duration_entry.bind("<FocusOut>", lambda event: add_placeholder(event, duration_entry, "optional"))
    duration_entry.place(x=250, y=150, width=100, height=30)

    Label(exercise_tab, text="Repetitions:", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=200)
    repetitions_entry = Entry(exercise_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    repetitions_entry.insert(0, "optional")
    repetitions_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, repetitions_entry))
    repetitions_entry.bind("<FocusOut>", lambda event: add_placeholder(event, repetitions_entry, "optional"))
    repetitions_entry.place(x=250, y=200, width=100, height=30)

    Label(exercise_tab, text="Sets:", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=250)
    sets_entry = Entry(exercise_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    sets_entry.insert(0, "optional")
    sets_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, sets_entry))
    sets_entry.bind("<FocusOut>", lambda event: add_placeholder(event, sets_entry, "optional"))
    sets_entry.place(x=250, y=250, width=100, height=30)

    def clear_placeholder(event, entry):
        if entry.get() == "optional":
            entry.delete(0, "end")
            entry.config(fg="#000716")

    def add_placeholder(event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#A9A9A9")

    def submit_exercise():
        date = date_entry.get()
        exercise = exercise_entry.get()
        duration = duration_entry.get()
        repetitions = repetitions_entry.get()
        sets = sets_entry.get()

        if duration == "optional":
            duration = ""
        if repetitions == "optional":
            repetitions = ""
        if sets == "optional":
            sets = ""

        if not duration and (not repetitions or not sets):
            print("Please provide either duration or both repetitions and sets.")
            return

        data_storage.data_storage["exercise"][date] = {
            "exercise": exercise,
            "duration": duration,
            "repetitions": repetitions,
            "sets": sets
        }
        data_storage.save_data(data_storage.data_storage)
        print(f"Date: {date}, Exercise: {exercise}, Duration: {duration} minutes, Repetitions: {repetitions}, Sets: {sets}")

    submit_button = Button(
        exercise_tab,
        text="Submit",
        borderwidth=0,
        highlightthickness=0,
        command=submit_exercise,
        relief="flat",
        bg="#FFD700",
        fg="#000000",
        font=("Arial-BoldMT", 14)
    )
    submit_button.place(x=150, y=300, width=100, height=30)

    exercise_tab.mainloop()

if __name__ == "__main__":
    open_exercise_tab()
