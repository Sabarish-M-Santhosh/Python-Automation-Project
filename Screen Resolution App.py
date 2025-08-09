import pyautogui
import tkinter as tk
from tkinter import messagebox

def show_resolution():
    size = pyautogui.size()
    messagebox.showinfo("Screen Resolution", f"Your screen resolution is {size.width} x {size.height}")

root = tk.Tk()
root.title("Screen Resolution Finder")
root.geometry("300x150")

btn=tk.Button(root, text="Find Screen Resolution", command=show_resolution, font=("Arial",12) )
btn.pack(pady=40)

root.mainloop()
