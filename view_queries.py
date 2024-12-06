import sqlite3

# Connect to the database
conn = sqlite3.connect('airline.db')
cursor = conn.cursor()

# 1. Query to select all flights
def select_all_flights():
    print("All flights:")
    cursor.execute("SELECT * FROM Flight")
    flights = cursor.fetchall()
    for flight in flights:
        print(flight)
    print("\n")

# 2. Query to count the number of passengers
def count_passengers():
    cursor.execute("SELECT COUNT(*) FROM Passenger")
    count = cursor.fetchone()[0]
    print(f"Total number of passengers: {count}\n")

# 3. Query to select reservations for a specific flight (example flight number 'DL303')
def reservations_for_flight(flight_number):
    print(f"Reservations for flight {flight_number}:")
    cursor.execute("SELECT * FROM Reservation WHERE FlightNumber = ?", (flight_number,))
    reservations = cursor.fetchall()
    for reservation in reservations:
        print(reservation)
    print("\n")

# 4. Query to update the seat number for a specific reservation
def update_seat_number(reservation_id, new_seat_number):
    cursor.execute("UPDATE Reservation SET SeatNumber = ? WHERE ReservationID = ?", (new_seat_number, reservation_id))
    conn.commit()
    print(f"Updated seat number for reservation ID {reservation_id} to {new_seat_number}\n")

# 5. Query to delete a reservation by ID
def delete_reservation(reservation_id):
    cursor.execute("DELETE FROM Reservation WHERE ReservationID = ?", (reservation_id,))
    conn.commit()
    print(f"Deleted reservation with ID {reservation_id}\n")

# 6. Query to retrieve all crew members assigned to a specific flight (example flight number 'DL303')
def crew_for_flight(flight_number):
    print(f"Crew for flight {flight_number}:")
    cursor.execute("""
        SELECT Crew.CrewID, Crew.CrewName, Crew.Position
        FROM Crew
        JOIN FlightCrew ON Crew.CrewID = FlightCrew.CrewID
        WHERE FlightCrew.FlightNumber = ?
    """, (flight_number,))
    crew_members = cursor.fetchall()
    for member in crew_members:
        print(member)
    print("\n")

# Run each query function with sample data
select_all_flights()
count_passengers()
reservations_for_flight("DL303")
update_seat_number(1, "15A")  # Example: Update reservation with ID 1 to seat 15A
delete_reservation(2)  # Example: Delete reservation with ID 2
crew_for_flight("DL303")

# Close the connection
conn.close()
