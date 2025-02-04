from tkinter import Tk, Canvas, Entry, Button, Label
from datetime import datetime
import data_storage

def open_track_steps_tab():
    track_steps_tab = Tk()
    track_steps_tab.geometry("393x852")
    track_steps_tab.configure(bg="#4E7DBB")
    track_steps_tab.title("Track Steps")

    canvas = Canvas(
        track_steps_tab,
        bg="#4E7DBB",
        height=852,
        width=393,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    Label(track_steps_tab, text="Date (YYYY-MM-DD):", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=50)
    date_entry = Entry(track_steps_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    date_entry.place(x=250, y=50, width=100, height=30)

    Label(track_steps_tab, text="Steps:", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=100)
    steps_entry = Entry(track_steps_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    steps_entry.place(x=150, y=100, width=200, height=30)

    def submit_steps():
        date = date_entry.get()
        steps = steps_entry.get()
        data_storage.data_storage["steps"][date] = steps
        data_storage.save_data(data_storage.data_storage)
        print(f"Date: {date}, Steps: {steps}")

    submit_button = Button(
        track_steps_tab,
        text="Submit",
        borderwidth=0,
        highlightthickness=0,
        command=submit_steps,
        relief="flat",
        bg="#FFD700",
        fg="#000000",
        font=("Arial-BoldMT", 14)
    )
    submit_button.place(x=150, y=150, width=100, height=30)

    track_steps_tab.mainloop()

if __name__ == "__main__":
    open_track_steps_tab()
