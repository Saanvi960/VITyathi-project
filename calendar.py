import calendar
import tkinter as tk
from tkinter import ttk, messagebox

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        self.year_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.event_var = tk.StringVar()

        self.year_var.set(calendar.datetime.datetime.now().year)
        self.month_var.set(calendar.datetime.datetime.now().month)

        self.create_widgets()
        self.load_events()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        ttk.Label(frame, text="Year:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.year_var, width=10).grid(row=0, column=1)

        ttk.Label(frame, text="Month:").grid(row=0, column=2, sticky="w")
        ttk.Entry(frame, textvariable=self.month_var, width=10).grid(row=0, column=3)

        ttk.Button(frame, text="Show Calendar", command=self.show_calendar).grid(row=0, column=4)

        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(padx=10, pady=10)

        self.event_frame = ttk.Frame(self.root)
        self.event_frame.pack(padx=10, pady=10)

        ttk.Label(self.event_frame, text="Date:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.event_frame, textvariable=self.date_var, width=10).grid(row=0, column=1)

        ttk.Label(self.event_frame, text="Event:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.event_frame, textvariable=self.event_var, width=30).grid(row=1, column=1)

        ttk.Button(self.event_frame, text="Add Event", command=self.add_event).grid(row=1, column=2)

    def show_calendar(self):
        year = int(self.year_var.get())
        month = int(self.month_var.get())
        cal_text = calendar.month(year, month)
        self.calendar_frame.destroy()
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(padx=10, pady=10)
        ttk.Label(self.calendar_frame, text=cal_text).grid(row=0, column=0)

    def add_event(self):
        date = self.date_var.get()
        event = self.event_var.get()

        if date and event:
            events = self.load_events()
            events[date] = event
            self.save_events(events)
            self.date_var.set("")
            self.event_var.set("")
            messagebox.showinfo("Success", "Event added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both date and event details.")

    def load_events(self):
        try:
            with open("events.txt", "r") as f:
                events = eval(f.read())
        except FileNotFoundError:
            events = {}
        return events

    def save_events(self, events):
        with open("events.txt", "w") as f:
            f.write(str(events))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
