# Calendar based date tracker

This is a simple yet powerful digital calendar application built entirely in Python. Designed for command-line interface (CLI) use, it provides an intuitive way to manage your schedule, events, and tasks directly from your terminal.
# Key Features:-
Event Scheduling: Easily add, modify, and delete events with specific dates and times.

Task Management: Differentiate between simple calendar events and persistent to-do list tasks.

Daily/Monthly View: Quick visualization of your schedule, either day-by-day or for the whole month.

Event Reminders: (If applicable) Set notifications for upcoming events.

Data Persistence: All events and tasks are saved (e.g., to a JSON or CSV file) so your calendar state is maintained across sessions.

 # The key technologies and tools used:-
 Core Python Modules:-
The functionality for displaying the calendar and manipulating dates is handled by two standard Python modules that come pre-installed.
datetime: This is the most crucial module for handling specific points in time. It is used to:
Get the current date and time.
Create, store, and compare specific event dates and times.
Perform arithmetic.
calendar: This module provides functions for working with calendars, which is essential for the display.

 Data Persistence:-
json (JSON format): The json module is used to easily serialize the Python objects into a human-readable text file and deserialize them back into Python objects when the program starts.
pickle (Python Object Serialization): Used to serialize complex Python objects directly into a binary file. This is easier for complex objects but is less human-readable and can have security risks.
sqlite3 (SQLite Database): For a more advanced project, this module allows using a small, file-based relational database to manage events, offering robust searching, filtering, and structured storage.

 CLI/Interface Enhancements (Optional but Common)
While the core application works with basic input/output, many developers use external libraries to make the CLI experience better:
argparse: Used to easily handle command-line arguments.
Click or Typer: Popular external libraries that simplify the creation of command-line interfaces, making it easier to structure the program with commands and sub-commands.
colorama: Used to add color and enhanced formatting to the terminal output, making the calendar views more visually appealing and easier to read.

# Steps to run the project:-
Ensure you have Python and the tkinter library installed on your system.
Navigate to the project directory: cd calendar-app
Run the application: python calendar.py

# Instructions for testing:-
Launch the application. Use the GUI to navigate through different months and years. To add an event, enter the date and event details in the designated fields and click "Add Event". View the calendar to see the added events highlighted on their respective dates.

# Screenshot:-
<img width="402" height="359" alt="image" src="https://github.com/user-attachments/assets/34b580a6-0837-487b-a275-a3f5ad9ca1d5" />
