import tkinter as ctk
from datetime import datetime, timedelta
import calendar

class ModernCalendarApp(ctk.Tk):
    def __init__(self):
        super().__init__()
        

        self.title("Modern Calendar")
        self.geometry("900x700")

        # ctk.set_appearance_mode("dark")
        # ctk.set_default_color_theme("blue")

        self.bg_primary = "#0f0f23"
        self.bg_secondary = "#1a1a2e"
        self.accent_purple = "#6d28d9"
        self.accent_pink = "#ec4899"
        self.accent_blue = "#3b82f6"
        self.card_bg = "#16213e"

        self.current_date = datetime.now()
        self.selected_date = None
        self.events = {}

        self.create_header()
        self.create_calendar_grid()
        self.create_event_panel()

        self.display_month()


def create_header(self):
    header_frame = ctk.TkFrame(self, fg_color="transparent")
    header_frame.pack(pady=20, padx=20, fill="x")

    self.prev_btn = ctk.TkButton(
        header_frame, text="<", width=50, font=("Arial", 20, "bold"),
        command=self.previous_month, fg_color=self.accent_purple
    )
    self.prev_btn.pack(side="left" , padx=10)

    self.month_year_label = ctk.TkLabel(
        header_frame, text="", font=("Arial", 28, "bold")
    )        
    self.month_year_label.pack(side="left", expand=True)

    self.today_btn = ctk.TkButton(
        header_frame, text="Today", width=100, font=("Arial", 14, "bold"),
        command=self.go_to_today, fg_color=self.accent_pink
    )
    self.today_btn.pack(side="left", padx=10)

    self.next_btn = ctk.TkButton(
        header_frame, text=">", width=50, font=("Arial", 20, "bold"),
        command=self.next_month, fg_color=self.accent_purple
    )
    self.next_btn.pack(side="left", padx=10)


def create_calendar_grid(self):
    self.calendar_frame = ctk.TkFrame(self, fg_color="transparent")
    self.calendar_frame.pack(pady=10, padx=20, fill="both", expand=True)

    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for col, day in enumerate(days):
        day_label = ctk.TkLabel(
            self.calendar_frame, text=day,
            font=("Arial", 14, "bold"), text_color=self.accent_pink
        )
        day_label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

    self.date_buttons = []
    for row in range(1, 7):
        week_buttons = []
        for col in range(7):
            btn = ctk.TkButton(
                self.calendar_frame, text="",
                width=100, height=80, font=("Arial", 16),
                fg_color=self.card_bg
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            week_buttons.append(btn)
        self.date_buttons.append(week_buttons)


def create_event_panel(self):
    event_frame = ctk.TkFrame(self, corner_radius=15)
    event_frame, text == "Events", font ==("Arial", 20, "bold")

    title_label = ctk.TkLabel(
        event_frame, text="Events", font=("Arial", 20, "bold")
    )
    title_label.pack(pady=15)

    self.selected_date_label = ctk.TkLabel(
        event_frame, text="Select a date", font=("Arial", 14)
    )
    self.selected_date_label.pack(pady=5)

    self.event_entry = ctk.TkEntry(
        event_frame, placeholder_text="Add new event...",
    font=("Arial", 14), height=40
    )
    self.event_entry.pack(pady=10, padx=20, fill="x")

    self.add_event_btn = ctk.TkButton(
        event_frame, text="Add Event",
        font=("Arial", 14, "bold"), command=self.add_event,
        fg_color=self.accent_purple, height=40
    )
    self.add_event_btn.pack(pady=5, padx=20, fill="x")

    self.events_textbox = ctk.TkTextbox(
        event_frame, font=("Arial", 13), wrap="word"
    )
    self.events_textbox.pack(pady=10, padx=20, fill="both", expand=True)


def display_month(self):
    month_name = self.current_date.strftime("%B %Y")
    self.month_year_label.configure(text=month_name)

    year = self.current_date.year
    month = self.current_date.month
    cal = calendar.monthcalendar(year, month)

    today = datetime.now()

    for week_idx, week in enumerate(cal):
        for day_idx, day in enumerate(week):
            btn = self.date_buttons[week_idx][day_idx]

            if day == 0:
                btn.configure(text="", state="disabled", fg_color=self.bbg_secondary)
            else:
                date_obj = datetime(year, month, day)
                date_str = date_obj.strftime("%Y-%m-%d")
                has_events = date_str in self.events

                if day == today.day and month == today.month and year == today.year:
                    fg_color = date_str in self.events
                elif has_events:
                    fg_color = "#10b981"
                else:
                    fg_color = self.card_bg

                btn.configure(
                    text=str(day), states="normal", fg_color=fg_color,
                    command=lambda d=date_obj: self.select_date(d)
                )


def select_date(self, date):
    self.selected_date = date
    date_str = date.strftime("%B $d, %Y")
    self.selected_date_label.configure(text=date_str)
    self.display_events()

def add_event(self):
    if not self.selected_date:
        return
    
    event_text = self.event_entry.get().strip()
    if not event_text:
        return
    
    date_key = self.selected_date.strftime("%Y-%m-%d")

    if date_key not in self.events:
        self.events[date_key] = []

    self.events[date_key].append(event_text) 
    self.event_entry.delete(0, "end")
    self.display_events()
    self.display_month()
    

def display_events(self):
    self.events_textbox.delete("1.0", "end")

    if not self.selected_date:
        return
    
    date_key = self.selected_date.strftime("%Y-%m-%d")

    if date_key in self.events:
        for ev in self.events[date_key]:
            self.events_textbook.insert("end", f". {ev}\n\n")
    else:
        self.events_textbook.insert("end", "No events for this day.")


def previous_month(self):
    if self.current_date.month == 1:
        self.current_date = self.current_date.replace(year=self.current_date.year - 1, month=12)
    else:
        self.current_date = self.current_date.replace(month=self.current_date.month - 1)
    self.display_month()

def next_month(self):
    if self.current_date.month == 12:
        self.current_date = self.current_date.replace(year=self.current_date.year + 1, month = 1)
    else:
        self.current_date = self.current_date.replace(month=self.current_date.month + 1)
    self.display_month()

def go_to_today(self):
    self.current_date = datetime.now()
    self.display_month()

if __name__ == "__main__":
    app = ModernCalendarApp()
    app.mainloop()
