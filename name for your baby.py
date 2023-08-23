import csv
import tkinter as tk
from tkinter import ttk

# Function to load names from a CSV file
def load_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        names = [row[1] for row in reader]
    return names

# Function to update the number input range based on gender selection
def update_number_range(*args):
    gender = gender_var.get()
    if gender == 'Male':
        number_entry.config(validate="key", validatecommand=(validate_command, "%P", 0, 14847))
    elif gender == 'Female':
        number_entry.config(validate="key", validatecommand=(validate_command, "%P", 0, 15384))

# Function to validate the number input within the specified range
def validate_number(P, min_value, max_value):
    try:
        num = int(P)
        return min_value <= num <= max_value
    except ValueError:
        return False

# Function to generate a name based on the selected gender and number
def generate_name():
    gender = gender_var.get()
    selected_number = int(number_entry.get())

    if gender == 'Male':
        names = male_names
    elif gender == 'Female':
        names = female_names
    else:
        result_label.config(text="Invalid gender selection")
        return

    if 0 <= selected_number <= len(names) - 1:
        selected_name = names[selected_number]
        result_label.config(text=f"Name #{selected_number} for {gender}: {selected_name}")
    else:
        result_label.config(text=f"Invalid number. Please enter a number between 0 and {len(names) - 1}.")

# Create a GUI window
root = tk.Tk()
root.title("Baby Name Generator")

# Load male and female names
male_names = load_names('Add the location of your saved csv file')
female_names = load_names('Add the location of your saved csv file')

# Create and configure GUI elements
gender_label = tk.Label(root, text="Select Gender:")
gender_label.pack()

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"])
gender_combobox.pack()

number_label = tk.Label(root, text="Enter a number:")
number_label.pack()

validate_command = root.register(validate_number)  # Register the validation function
number_entry = tk.Entry(root, validate="key", validatecommand=(validate_command, "%P", 0, 14847))  # Default range for Male
number_entry.pack()

gender_var.trace_add('write', update_number_range)  # Trigger the update when gender changes

generate_button = tk.Button(root, text="Generate Name", command=generate_name)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
