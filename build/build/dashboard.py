# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
import subprocess
from datetime import datetime
import time

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, PhotoImage, Button, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\jpcat\Downloads\build\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_exercise_tab():
    subprocess.run(["python", str(OUTPUT_PATH / "exercise.py")])

def open_current_status_tab():
    subprocess.run(["python", str(OUTPUT_PATH / "current_status.py")])

def open_water_intake_tab():
    subprocess.run(["python", str(OUTPUT_PATH / "water_intake.py")])

def open_track_steps_tab():
    subprocess.run(["python", str(OUTPUT_PATH / "track_steps.py")])

def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    canvas.itemconfig(time_label, text=current_time)
    window.after(1000, update_time)

window = Tk()

window.geometry("393x852")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 852,
    width = 393,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    393.0,
    852.0,
    fill="#4E7DBB",
    outline=""
)

canvas.create_text(
    196.0,
    50.0,
    text="Welcome to the Dashboard",
    fill="#FFFFFF",
    font=("Arial-BoldMT", 24)
)

# Real-time Date and Time
time_label = canvas.create_text(
    196.0,
    100.0,
    text="",
    fill="#FFFFFF",
    font=("Arial-BoldMT", 16)
)
update_time()

# Water Intake Button
water_intake_button = Button(
    text="Water Intake",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=open_water_intake_tab,
    bg="#FFD700",
    fg="#000000",
    font=("Arial-BoldMT", 14)
)
water_intake_button.place(
    x=120.0,
    y=300.0,
    width=162.0,
    height=50.0
)

# Exercise Button
exercise_button = Button(
    text="Exercise",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=open_exercise_tab,
    bg="#FFD700",
    fg="#000000",
    font=("Arial-BoldMT", 14)
)
exercise_button.place(
    x=120.0,
    y=400.0,
    width=162.0,
    height=50.0
)

# Status Button
current_status_button = Button(
    text="Status",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=open_current_status_tab,
    bg="#FFD700",
    fg="#000000",
    font=("Arial-BoldMT", 14)
)
current_status_button.place(
    x=120.0,
    y=500.0,
    width=162.0,
    height=50.0
)

# Track Steps Button
track_steps_button = Button(
    text="Track Steps",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=open_track_steps_tab,
    bg="#FFD700",
    fg="#000000",
    font=("Arial-BoldMT", 14)
)
track_steps_button.place(
    x=120.0,
    y=600.0,
    width=162.0,
    height=50.0
)

window.resizable(False, False)
window.mainloop()
