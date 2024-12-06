import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('airline.db')
cursor = conn.cursor()

# Additional Sample Data for Aircraft Table
cursor.execute("INSERT INTO Aircraft (AircraftID, AircraftType, RegistrationNumber, MaintenanceSchedule, LastMaintenanceDate) VALUES (3, 'Boeing 777', 'N54321', 'Every 6 months', '2023-03-10')")
cursor.execute("INSERT INTO Aircraft (AircraftID, AircraftType, RegistrationNumber, MaintenanceSchedule, LastMaintenanceDate) VALUES (4, 'Airbus A330', 'N98765', 'Every 12 months', '2023-02-28')")

# Additional Sample Data for Crew Table
cursor.execute("INSERT INTO Crew (CrewID, CrewName, ContactInfo, Position, Certification) VALUES (3, 'Paul Roberts', 'paul.roberts@example.com', 'Pilot', 'FAA Certified')")
cursor.execute("INSERT INTO Crew (CrewID, CrewName, ContactInfo, Position, Certification) VALUES (4, 'Susan Miller', 'susan.miller@example.com', 'Flight Attendant', 'Safety Certified')")
cursor.execute("INSERT INTO Crew (CrewID, CrewName, ContactInfo, Position, Certification) VALUES (5, 'Emily Davis', 'emily.davis@example.com', 'Co-Pilot', 'FAA Certified')")
cursor.execute("INSERT INTO Crew (CrewID, CrewName, ContactInfo, Position, Certification) VALUES (6, 'Michael Johnson', 'michael.johnson@example.com', 'Flight Attendant', 'Safety Certified')")

# Additional Sample Data for Passenger Table
cursor.execute("INSERT INTO Passenger (PassengerID, PassengerName, ContactInfo, FrequentFlyerNumber, LoyaltyStatus) VALUES (3, 'Charles Green', 'charles.green@example.com', 'FF54321', 'Bronze')")
cursor.execute("INSERT INTO Passenger (PassengerID, PassengerName, ContactInfo, FrequentFlyerNumber, LoyaltyStatus) VALUES (4, 'Diana White', 'diana.white@example.com', 'FF67891', 'Gold')")
cursor.execute("INSERT INTO Passenger (PassengerID, PassengerName, ContactInfo, FrequentFlyerNumber, LoyaltyStatus) VALUES (5, 'Eric Brown', 'eric.brown@example.com', 'FF11223', 'Silver')")
cursor.execute("INSERT INTO Passenger (PassengerID, PassengerName, ContactInfo, FrequentFlyerNumber, LoyaltyStatus) VALUES (6, 'Fiona Black', 'fiona.black@example.com', 'FF99876', 'Platinum')")

# Additional Sample Data for MaintenanceTask Table
cursor.execute("INSERT INTO MaintenanceTask (TaskID, TaskDescription, FrequencyInterval) VALUES (3, 'Landing Gear Inspection', 'Annually')")
cursor.execute("INSERT INTO MaintenanceTask (TaskID, TaskDescription, FrequencyInterval) VALUES (4, 'Electrical System Check', 'Quarterly')")

# Additional Sample Data for Flight Table
cursor.execute("INSERT INTO Flight (FlightNumber, DepartureAirport, ArrivalAirport, DepartureDateTime, ArrivalDateTime, AircraftID, CrewID) VALUES ('DL303', 'ATL', 'LHR', '2023-07-17 17:00:00', '2023-07-18 07:00:00', 3, 3)")
cursor.execute("INSERT INTO Flight (FlightNumber, DepartureAirport, ArrivalAirport, DepartureDateTime, ArrivalDateTime, AircraftID, CrewID) VALUES ('AF404', 'CDG', 'JFK', '2023-07-18 10:30:00', '2023-07-18 13:30:00', 4, 4)")
cursor.execute("INSERT INTO Flight (FlightNumber, DepartureAirport, ArrivalAirport, DepartureDateTime, ArrivalDateTime, AircraftID, CrewID) VALUES ('BA505', 'LHR', 'DXB', '2023-07-19 20:00:00', '2023-07-20 04:00:00', 1, 5)")
cursor.execute("INSERT INTO Flight (FlightNumber, DepartureAirport, ArrivalAirport, DepartureDateTime, ArrivalDateTime, AircraftID, CrewID) VALUES ('EK606', 'DXB', 'SYD', '2023-07-20 22:00:00', '2023-07-21 06:00:00', 2, 6)")


# Additional Sample Data for Reservation Table
cursor.execute("INSERT INTO Reservation (ReservationID, PassengerName, ContactInfo, FlightNumber, SeatNumber, FareClass) VALUES (3, 'Charles Green', 'charles.green@example.com', 'DL303', '16C', 'Economy')")
cursor.execute("INSERT INTO Reservation (ReservationID, PassengerName, ContactInfo, FlightNumber, SeatNumber, FareClass) VALUES (4, 'Diana White', 'diana.white@example.com', 'AF404', '5A', 'Business')")
cursor.execute("INSERT INTO Reservation (ReservationID, PassengerName, ContactInfo, FlightNumber, SeatNumber, FareClass) VALUES (5, 'Eric Brown', 'eric.brown@example.com', 'BA505', '23B', 'Economy')")
cursor.execute("INSERT INTO Reservation (ReservationID, PassengerName, ContactInfo, FlightNumber, SeatNumber, FareClass) VALUES (6, 'Fiona Black', 'fiona.black@example.com', 'EK606', '1A', 'First')")

# Additional Sample Data for FlightCrew Table
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('DL303', 3)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('DL303', 5)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('AF404', 4)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('AF404', 6)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('BA505', 1)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('BA505', 6)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('EK606', 2)")
cursor.execute("INSERT INTO FlightCrew (FlightNumber, CrewID) VALUES ('EK606', 3)")

# Additional Sample Data for AircraftMaintenance Table
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (1, 3)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (1, 4)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (2, 3)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (2, 4)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (3, 1)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (3, 2)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (4, 1)")
cursor.execute("INSERT INTO AircraftMaintenance (AircraftID, TaskID) VALUES (4, 2)")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Additional sample data added successfully.")
