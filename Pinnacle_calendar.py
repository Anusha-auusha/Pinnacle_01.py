import tkinter as tk
from tkinter import simpledialog, messagebox
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Calendar with Reminders")

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.reminders = {}

        self.create_widgets()
        self.display_calendar()

    def create_widgets(self):
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()

        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack()

        self.prev_button = tk.Button(self.nav_frame, text="<", command=self.prev_month)
        self.prev_button.pack(side="left")

        self.month_label = tk.Label(self.nav_frame, text="")
        self.month_label.pack(side="left")

        self.next_button = tk.Button(self.nav_frame, text=">", command=self.next_month)
        self.next_button.pack(side="left")

    def display_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.month_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

        cal = calendar.monthcalendar(self.current_year, self.current_month)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            tk.Label(self.calendar_frame, text=day).grid(row=0, column=days.index(day))

        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day != 0:
                    day_button = tk.Button(self.calendar_frame, text=str(day), width=4, height=2,
                                           command=lambda d=day: self.add_reminder(d))
                    day_button.grid(row=i+1, column=j)
                    if (self.current_year, self.current_month, day) in self.reminders:
                        day_button.config(bg="yellow")

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.display_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.display_calendar()

    def add_reminder(self, day):
        date = (self.current_year, self.current_month, day)
        reminder_text = simpledialog.askstring("Add Reminder", f"Enter reminder for {calendar.month_name[self.current_month]} {day}, {self.current_year}:")
        if reminder_text:
            self.reminders[date] = reminder_text
            self.display_calendar()

    def show_reminders(self, day):
        date = (self.current_year, self.current_month, day)
        if date in self.reminders:
            messagebox.showinfo("Reminders", f"Reminders for {calendar.month_name[self.current_month]} {day}, {self.current_year}:\n\n{self.reminders[date]}")
        else:
            messagebox.showinfo("Reminders", f"No reminders for {calendar.month_name[self.current_month]} {day}, {self.current_year}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
