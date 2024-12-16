import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import threading

# Function to get available serial ports
def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

# Function to auto-refresh serial ports
def refresh_serial_ports():
    while True:
        serial_ports = get_serial_ports()
        serial_port['values'] = serial_ports
        if serial_ports:
            serial_port.set(serial_ports[0])  # Set default if available
        window.after(5000, refresh_serial_ports)  # Refresh every 5 seconds
        break

# Function to send data to the serial port
def send_data(command):
    try:
        port = serial.Serial(serial_port.get(), baudrate=9600, timeout=1)
        port.write(command.encode())
        response = port.readline().decode('utf-8').strip()
        update_serial_monitor(response)
        port.close()
    except Exception as e:
        messagebox.showerror("Serial Error", f"Error communicating with serial port: {e}")

# Function to update the serial monitor
def update_serial_monitor(message):
    # Update the serial monitor, keep it limited to 4 lines
    serial_monitor.insert(tk.END, message + '\n')
    if int(serial_monitor.index('end-1c').split('.')[0]) > 4:
        serial_monitor.delete(1.0, 2.0)  # Remove the oldest line

# Validate address format (00-99)
def validate_address(address):
    return len(address) == 2 and address.isdigit() and 0 <= int(address) <= 99

# Handle placeholder text for entry fields
def handle_placeholder(event, entry, placeholder_text):
    if entry.get() == placeholder_text:  # If the box has placeholder text
        entry.delete(0, tk.END)  # Clear the placeholder
        entry.config(fg="black")  # Set input text to black

def restore_placeholder(event, entry, placeholder_text):
    if not entry.get():  # If the box is empty after losing focus
        entry.insert(0, placeholder_text)  # Restore placeholder
        entry.config(fg="gray")  # Set placeholder text to gray

# Feed handler (send "Fxx")
def feed():
    address = address_entry.get()
    if validate_address(address):
        send_data(f"F{address}")  # Prefix with F and send
    else:
        messagebox.showerror("Invalid Address", "Incorrect format. Please enter a valid feeder address (00-99).")

# Program address handler (send "Axx" after warning)
def program_address():
    address = address_entry.get()
    if validate_address(address):
        show_warning(address)  # Show warning before proceeding
    else:
        messagebox.showerror("Invalid Address", "Incorrect format. Please enter a valid feeder address (00-99).")

# Warning popup for Program Address
def show_warning(address):
    def proceed_program():
        send_data(f"A{address}")  # Prefix with A and send after proceed
        warning_window.destroy()

    def cancel_program():
        warning_window.destroy()

    warning_window = tk.Toplevel(window)
    warning_window.title("Warning")
    warning_window.geometry("350x150")
    warning_window.config(bg="#cc0000")

    message_label = tk.Label(
        warning_window, 
        text="Connect only one feeder at a time.\nMultiple feeders may cause errors.",
        bg="#cc0000", 
        fg="white", 
        font=("Arial", 12), 
        wraplength=300, 
        justify="center"
    )
    message_label.pack(padx=10, pady=20)

    # Proceed button red, Cancel button green
    proceed_button = tk.Button(warning_window, text="Proceed", command=proceed_program, bg="red", fg="white")
    cancel_button = tk.Button(warning_window, text="Cancel", command=cancel_program, bg="green", fg="white")

    cancel_button.pack(side=tk.LEFT, padx=20, pady=10)
    proceed_button.pack(side=tk.RIGHT, padx=20, pady=10)

# Setup main window
window = tk.Tk()
window.title("FeederControl")  # Updated window title without dash

# Dark Mode Styling
window.config(bg="#121212")
window.geometry("500x400")

# Serial Port Dropdown
serial_ports = get_serial_ports()
serial_port = ttk.Combobox(window, values=serial_ports, width=30)
serial_port.set(serial_ports[0] if serial_ports else "No Ports Available")
serial_port.grid(row=0, column=0, padx=10, pady=10)

# Feed Button
feed_button = tk.Button(window, text="Feed", command=feed, bg="#4CAF50", fg="white")
feed_button.grid(row=1, column=0, padx=10, pady=10)

# Address Entry Box (for both Feed and Program Address Buttons)
address_entry = tk.Entry(window, bg="#2c2c2c", fg="gray", insertbackground='white')
address_placeholder = "00"
address_entry.insert(0, address_placeholder)
address_entry.bind("<FocusIn>", lambda e: handle_placeholder(e, address_entry, address_placeholder))
address_entry.bind("<FocusOut>", lambda e: restore_placeholder(e, address_entry, address_placeholder))
address_entry.grid(row=1, column=1, padx=10, pady=10)

# Program Address Button
program_button = tk.Button(window, text="Program Address", command=program_address, bg="#f44336", fg="white")
program_button.grid(row=2, column=0, padx=10, pady=10)

# Serial Monitor Box
serial_monitor = tk.Text(window, height=4, width=50, bg="#2c2c2c", fg="white")
serial_monitor.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Footer
footer_label = tk.Label(window, text="FEEDER CONTROL - CREATED BY ADAM KIRBY", bg="#121212", fg="white", font=("Arial", 10))
footer_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Start the serial port refreshing thread
threading.Thread(target=refresh_serial_ports, daemon=True).start()

# Start the Tkinter event loop
window.mainloop()

