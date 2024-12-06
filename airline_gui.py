import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Airline Management System")
root.geometry("800x600")

# Load and set the background image
background_image = Image.open("background.jpg")
background_image = background_image.resize((800, 600), Image.LANCZOS)  # Resize to fit the window
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Frame to contain the content over the background
main_frame = tk.Frame(root, bg="#003366", bd=5)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

# Connect to the database
def connect_db():
    conn = sqlite3.connect('airline.db')
    return conn

# Add New Passenger Function
def add_passenger():
    add_window = tk.Toplevel(root)
    add_window.title("Add New Passenger")
    add_window.geometry("400x300")
    add_window.configure(bg="#e6f7ff")

    tk.Label(add_window, text="First Name", bg="#e6f7ff").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Last Name", bg="#e6f7ff").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Contact Info", bg="#e6f7ff").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Frequent Flyer Number", bg="#e6f7ff").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Loyalty Status", bg="#e6f7ff").grid(row=4, column=0, padx=10, pady=5)

    first_name = tk.Entry(add_window)
    last_name = tk.Entry(add_window)
    contact_info = tk.Entry(add_window)
    ff_number = tk.Entry(add_window)
    loyalty_status = tk.Entry(add_window)

    first_name.grid(row=0, column=1, padx=10, pady=5)
    last_name.grid(row=1, column=1, padx=10, pady=5)
    contact_info.grid(row=2, column=1, padx=10, pady=5)
    ff_number.grid(row=3, column=1, padx=10, pady=5)
    loyalty_status.grid(row=4, column=1, padx=10, pady=5)

    def submit_passenger():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Passenger (PassengerName, ContactInfo, FrequentFlyerNumber, LoyaltyStatus) VALUES (?, ?, ?, ?)",
                       (first_name.get() + " " + last_name.get(), contact_info.get(), ff_number.get(), loyalty_status.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Passenger added successfully.")
        add_window.destroy()

    tk.Button(add_window, text="Add Passenger", command=submit_passenger, bg="#003366", fg="dark blue").grid(row=5, column=1, pady=10)

# Add New Reservation Function
# Add New Reservation Function
def add_reservation():
    reservation_window = tk.Toplevel(root)
    reservation_window.title("Add New Reservation")
    reservation_window.geometry("400x300")
    reservation_window.configure(bg="#e6f7ff")

    tk.Label(reservation_window, text="Passenger Name", bg="#e6f7ff").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(reservation_window, text="Contact Info", bg="#e6f7ff").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(reservation_window, text="Flight Number", bg="#e6f7ff").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(reservation_window, text="Seat Number", bg="#e6f7ff").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(reservation_window, text="Fare Class", bg="#e6f7ff").grid(row=4, column=0, padx=10, pady=5)

    passenger_name = tk.Entry(reservation_window)
    contact_info = tk.Entry(reservation_window)
    flight_number = tk.Entry(reservation_window)
    seat_number = tk.Entry(reservation_window)
    fare_class = tk.Entry(reservation_window)

    passenger_name.grid(row=0, column=1, padx=10, pady=5)
    contact_info.grid(row=1, column=1, padx=10, pady=5)
    flight_number.grid(row=2, column=1, padx=10, pady=5)
    seat_number.grid(row=3, column=1, padx=10, pady=5)
    fare_class.grid(row=4, column=1, padx=10, pady=5)

    def submit_reservation():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Reservation (PassengerName, ContactInfo, FlightNumber, SeatNumber, FareClass) VALUES (?, ?, ?, ?, ?)",
                       (passenger_name.get(), contact_info.get(), flight_number.get(), seat_number.get(), fare_class.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation added successfully.")
        reservation_window.destroy()

    # Button with text "Add Reservation"
    tk.Button(reservation_window, text="Add Reservation", command=submit_reservation, bg="#003366", fg="dark blue").grid(row=5, column=1, pady=10)

# Define other functions here, like view_flights, update_reservation, delete_reservation...
# View Flights Function
from tkinter import ttk

# View Flights Function
def view_flights():
    view_window = tk.Toplevel(root)
    view_window.title("View All Flights")
    view_window.geometry("600x400")
    view_window.configure(bg="#ffffff")

    # Create a Treeview widget
    tree = ttk.Treeview(view_window, columns=("FlightNumber", "Departure", "Arrival", "DepartureTime", "ArrivalTime", "AircraftID", "CrewID"), show="headings")
    tree.heading("FlightNumber", text="Flight Number")
    tree.heading("Departure", text="Departure")
    tree.heading("Arrival", text="Arrival")
    tree.heading("DepartureTime", text="Departure Time")
    tree.heading("ArrivalTime", text="Arrival Time")
    tree.heading("AircraftID", text="Aircraft ID")
    tree.heading("CrewID", text="Crew ID")

    # Set column widths
    tree.column("FlightNumber", width=100)
    tree.column("Departure", width=100)
    tree.column("Arrival", width=100)
    tree.column("DepartureTime", width=150)
    tree.column("ArrivalTime", width=150)
    tree.column("AircraftID", width=100)
    tree.column("CrewID", width=100)

    # Fetch data from database and insert into the tree
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flight")
    flights = cursor.fetchall()
    conn.close()

    for flight in flights:
        tree.insert("", "end", values=flight)

    # Pack the Treeview widget and add a scrollbar
    tree.pack(fill="both", expand=True)

    # Adding Scrollbar for Treeview
    scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

# Update Reservation Function
def update_reservation():
    update_window = tk.Toplevel(root)
    update_window.title("Update Reservation")
    update_window.geometry("400x200")
    update_window.configure(bg="#e6f7ff")

    tk.Label(update_window, text="Reservation ID", bg="#e6f7ff").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(update_window, text="New Flight Number", bg="#e6f7ff").grid(row=1, column=0, padx=10, pady=5)

    reservation_id = tk.Entry(update_window)
    new_flight_number = tk.Entry(update_window)

    reservation_id.grid(row=0, column=1, padx=10, pady=5)
    new_flight_number.grid(row=1, column=1, padx=10, pady=5)

    def submit_update():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE Reservation SET FlightNumber = ? WHERE ReservationID = ?", (new_flight_number.get(), reservation_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation updated successfully.")
        update_window.destroy()

    tk.Button(update_window, text="Update Reservation", command=submit_update, bg="#003366", fg="dark blue").grid(row=2, column=1, pady=10)

# Delete Reservation Function
def delete_reservation():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Reservation")
    delete_window.geometry("400x150")
    delete_window.configure(bg="#e6f7ff")

    tk.Label(delete_window, text="Reservation ID", bg="#e6f7ff").grid(row=0, column=0, padx=10, pady=5)
    reservation_id = tk.Entry(delete_window)
    reservation_id.grid(row=0, column=1, padx=10, pady=5)

    def submit_delete():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Reservation WHERE ReservationID = ?", (reservation_id.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation deleted successfully.")
        delete_window.destroy()

    tk.Button(delete_window, text="Delete Reservation", command=submit_delete, bg="#003366", fg="dark blue").grid(row=1, column=1, pady=10)

# Button styles and placement on the main window
button_style = {"bg": "white", "fg": "dark blue", "font": ("Arial", 12, "bold"), "width": 20, "height": 2}

add_passenger_button = tk.Button(main_frame, text="Add Passenger", command=add_passenger)
add_passenger_button.config(**button_style)
add_passenger_button.pack(pady=10)

add_reservation_button = tk.Button(main_frame, text="Add Reservation", command=add_reservation)
add_reservation_button.config(**button_style)
add_reservation_button.pack(pady=10)

view_flights_button = tk.Button(main_frame, text="View Flights", command=view_flights)
view_flights_button.config(**button_style)
view_flights_button.pack(pady=10)

update_reservation_button = tk.Button(main_frame, text="Update Reservation", command=update_reservation)
update_reservation_button.config(**button_style)
update_reservation_button.pack(pady=10)

delete_reservation_button = tk.Button(main_frame, text="Delete Reservation", command=delete_reservation)
delete_reservation_button.config(**button_style)
delete_reservation_button.pack(pady=10)

# Run the main loop
root.mainloop()
