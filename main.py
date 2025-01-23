import tkinter as tk
from tkinter import messagebox
import random
import string
import json
import os

# File to store saved passwords
PASSWORD_FILE = "passwords.json"

# Load existing passwords from file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save passwords to file
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)

# Generate Password
def generate_password():
    length = 16  # Minimum length of the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Save the generated password with a label
def save_password():
    password = password_entry.get()
    label = label_entry.get()
    
    if password and label:
        passwords = load_passwords()
        passwords[label] = password
        save_passwords(passwords)
        messagebox.showinfo("Password Saved", f"Password for {label} has been saved!")
        label_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        update_saved_passwords()
    else:
        messagebox.showwarning("Input Error", "Please enter both label and password.")

# Display saved passwords in the list
def update_saved_passwords():
    passwords = load_passwords()
    saved_passwords.delete(1.0, tk.END)  # Clear the current list
    for label, password in passwords.items():
        saved_passwords.insert(tk.END, f"{label}: {password}\n")

# Delete a password from the saved list
def delete_password():
    label = label_entry.get()
    
    if label:
        passwords = load_passwords()
        if label in passwords:
            del passwords[label]
            save_passwords(passwords)
            messagebox.showinfo("Password Deleted", f"Password for {label} has been deleted.")
            label_entry.delete(0, tk.END)
            update_saved_passwords()
        else:
            messagebox.showwarning("Not Found", f"No password found for {label}.")
    else:
        messagebox.showwarning("Input Error", "Please enter a label to delete.")

# Copy a password to the clipboard
def copy_password():
    label = label_entry.get()
    passwords = load_passwords()
    
    if label in passwords:
        root.clipboard_clear()
        root.clipboard_append(passwords[label])
        messagebox.showinfo("Password Copied", f"Password for {label} has been copied to clipboard.")
    else:
        messagebox.showwarning("Not Found", f"No password found for {label}.")

# Create the main window
root = tk.Tk()
root.title("Password Manager / Generator")

# Set up window size and background color
root.geometry("600x900")
root.config(bg="#2b2b2b")

# Banner Frame
banner_frame = tk.Frame(root, bg="#00b4ff", height=100)
banner_frame.pack(fill=tk.X)

# Banner Label
banner_label = tk.Label(banner_frame, text="Password Manager / Generator", font=("Arial", 24, "bold"), fg="#ffffff", bg="#00b4ff")
banner_label.pack(pady=20)

# Password Display Entry
password_entry = tk.Entry(root, font=("Arial", 16), width=30, bg="#252525", fg="#ffffff", bd=2, relief="flat", justify="center")
password_entry.pack(pady=20)

# Label Entry
label_entry = tk.Entry(root, font=("Arial", 16), width=30, bg="#252525", fg="#ffffff", bd=2, relief="flat", justify="center")
label_entry.pack(pady=10)

# Generate Password Button (with bevel)
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14, "bold"), bg="#00b4ff", fg="#ffffff", relief="sunken", bd=5, command=generate_password)
generate_button.pack(pady=10)

# Save Password Button (with bevel)
save_button = tk.Button(root, text="Save Password", font=("Arial", 14, "bold"), bg="#00b4ff", fg="#ffffff", relief="sunken", bd=5, command=save_password)
save_button.pack(pady=10)

# Copy Password Button (with bevel)
copy_button = tk.Button(root, text="Copy Password", font=("Arial", 14, "bold"), bg="#ff6600", fg="#ffffff", relief="sunken", bd=5, command=copy_password)
copy_button.pack(pady=10)

# Delete Password Button (with bevel)
delete_button = tk.Button(root, text="Delete Password", font=("Arial", 14, "bold"), bg="#ff6600", fg="#ffffff", relief="sunken", bd=5, command=delete_password)
delete_button.pack(pady=10)

# Display Saved Passwords
saved_passwords_label = tk.Label(root, text="Saved Passwords", font=("Arial", 14, "bold"), fg="#ffffff", bg="#2b2b2b")
saved_passwords_label.pack(pady=10)

saved_passwords = tk.Text(root, font=("Arial", 12), width=45, height=10, bg="#252525", fg="#ffffff", bd=2, relief="flat")
saved_passwords.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Created by IXRMTT", font=("Arial", 10), fg="#bbb", bg="#2b2b2b")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Update the saved passwords list on startup
update_saved_passwords()

# Start the Tkinter event loop
root.mainloop()
