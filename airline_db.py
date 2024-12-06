import sqlite3

# Connect to SQLite database (creates it if it doesn’t exist)
conn = sqlite3.connect('airline.db')
cursor = conn.cursor()

# Create tables
# Flight Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Flight (
        FlightNumber VARCHAR(10) PRIMARY KEY,
        DepartureAirport VARCHAR(10),
        ArrivalAirport VARCHAR(10),
        DepartureDateTime DATETIME,
        ArrivalDateTime DATETIME,
        AircraftID INT,
        CrewID INT,
        FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID)
    )
''')

# Reservation Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reservation (
        ReservationID INTEGER PRIMARY KEY,
        PassengerName VARCHAR(255),
        ContactInfo VARCHAR(255),
        FlightNumber VARCHAR(10),
        SeatNumber VARCHAR(10),
        FareClass VARCHAR(50),
        FOREIGN KEY (FlightNumber) REFERENCES Flight(FlightNumber)
    )
''')

# Passenger Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Passenger (
        PassengerID INTEGER PRIMARY KEY,
        PassengerName VARCHAR(255),
        ContactInfo VARCHAR(255),
        FrequentFlyerNumber VARCHAR(50) ,
        LoyaltyStatus VARCHAR(50)
    )
''')

# Crew Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Crew (
        CrewID INTEGER PRIMARY KEY,
        CrewName VARCHAR(255),
        ContactInfo VARCHAR(255),
        Position VARCHAR(50),
        Certification VARCHAR(255)
    )
''')

# Aircraft Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aircraft (
        AircraftID INTEGER PRIMARY KEY,
        AircraftType VARCHAR(50),
        RegistrationNumber VARCHAR(50),
        MaintenanceSchedule VARCHAR(255),
        LastMaintenanceDate DATE
    )
''')

# MaintenanceTask Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaintenanceTask (
        TaskID INTEGER PRIMARY KEY,
        TaskDescription VARCHAR(255),
        FrequencyInterval VARCHAR(50)
    )
''')

# FlightCrew Table (for Many-to-Many relationship between Flight and Crew)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FlightCrew (
        FlightNumber VARCHAR(10),
        CrewID INTEGER,
        PRIMARY KEY (FlightNumber, CrewID),
        FOREIGN KEY (FlightNumber) REFERENCES Flight(FlightNumber),
        FOREIGN KEY (CrewID) REFERENCES Crew(CrewID)
    )
''')

# AircraftMaintenance Table (for Many-to-Many relationship between Aircraft and MaintenanceTask)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS AircraftMaintenance (
        AircraftID INTEGER,
        TaskID INTEGER,
        PRIMARY KEY (AircraftID, TaskID),
        FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID),
        FOREIGN KEY (TaskID) REFERENCES MaintenanceTask(TaskID)
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")
