from tkinter import Tk, Canvas, Entry, Button, Label
from datetime import datetime
import data_storage

def open_water_intake_tab():
    water_intake_tab = Tk()
    water_intake_tab.geometry("393x852")
    water_intake_tab.configure(bg="#4E7DBB")
    water_intake_tab.title("Water Intake")

    canvas = Canvas(
        water_intake_tab,
        bg="#4E7DBB",
        height=852,
        width=393,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    Label(water_intake_tab, text="Date (YYYY-MM-DD):", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=50)
    date_entry = Entry(water_intake_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    date_entry.place(x=250, y=50, width=100, height=30)

    Label(water_intake_tab, text="Water Intake (ml):", bg="#4E7DBB", fg="#FFFFFF", font=("Arial-BoldMT", 16)).place(x=50, y=100)
    water_entry = Entry(water_intake_tab, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    water_entry.place(x=250, y=100, width=100, height=30)

    def submit_water_intake():
        date = date_entry.get()
        intake = water_entry.get()
        data_storage.data_storage["water_intake"][date] = intake
        data_storage.save_data(data_storage.data_storage)
        print(f"Date: {date}, Water Intake: {intake} ml")

    submit_button = Button(
        water_intake_tab,
        text="Submit",
        borderwidth=0,
        highlightthickness=0,
        command=submit_water_intake,
        relief="flat",
        bg="#FFD700",
        fg="#000000",
        font=("Arial-BoldMT", 14)
    )
    submit_button.place(x=150, y=150, width=100, height=30)

    water_intake_tab.mainloop()

if __name__ == "__main__":
    open_water_intake_tab()
