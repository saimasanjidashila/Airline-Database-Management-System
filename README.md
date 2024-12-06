# CSC4402_project_airlinedbms

GitHub link: https://github.com/Nurjahan-Nipa/CSC4402_project_airlinedbms/tree/main

Group Members:
Nurjahan, Nurjahan (nurja1@lsu.edu)
Saima Sanjida Shila (sshila1@lsu.edu)
Kaushani Samarawickrama (ksamar2@lsu.edu)

# Airline Database Management System

This project is an Airline Management System developed using Python, SQLite, and LaTeX for report generation. The system is designed to manage passengers, flights, reservations, crew, aircraft, and maintenance tasks efficiently.

### Database Tables:
- **Passenger**: Stores passenger details.
- **Flight**: Tracks flight schedules and aircraft/crew associations.
- **Reservation**: Manages passenger reservations.
- **Crew**: Stores crew member details.
- **Aircraft**: Tracks aircraft information and maintenance tasks.
- **MaintenanceTask**: Defines maintenance tasks.
- **FlightCrew**: Many-to-many relationship between flights and crew.
- **AircraftMaintenance**: Many-to-many relationship between aircraft and maintenance tasks.

---

## Getting Started

### Prerequisites:
- Python 3.9 or higher
- DB Browser for SQLite
- LaTeX distribution (e.g., TeX Live, MikTeX, or Overleaf)

### Platform
Visual Studio Code/Jupyter; 

### Instructions:

First, you have to run airline_gui.py file to perform various operations like addition, update, delete, view.
To retrive specific queries, you need to open the database in dbbrowser for SQLite, then go to the execute SQL panel and run the following tets queries.


### Code Files

There are four python files in this project: airline_gui.py, airline_db.py, add_data_db.py, view_queries.py. The airline_gui.py is for generating the graphical user interface, connecting the background database file, defining functions for each modules like add, update, delete, view. The airline_db.py is for creating the tables for database and add_data_db.py is used for inserting values to the database. The view_queries.py contains some basic query.

** Database File**

airline.db

### Test Queries

Query-1: To retrieve the data values from crew table, we used 
    SELECT * from Crew
Query-2: To view the flight details we can mention the attributes in the select clause:
 
    SELECT FlightNumber, DepartureAirport, ArrivalAirport, 
    DepartureDateTime, ArrivalDateTime
    FROM Flight;
    
Query-3: We can search passengers by loyalty status by using the query as: 

    SELECT PassengerName, LoyaltyStatus 
    FROM Passenger 
    WHERE LoyaltyStatus = 'Gold';
    
Query-4: Retrieving flights with crew members can be queried in this way:
    
    SELECT f.FlightNumber, c.CrewName, c.Position
    FROM Flight f
    JOIN FlightCrew fc ON f.FlightNumber = fc.FlightNumber
    JOIN Crew c ON fc.CrewID = c.CrewID;
    
Query-5: To view the passengers with reservation, we can query like this:
   
    SELECT p.PassengerName, r.FlightNumber, r.SeatNumber, r.FareClass
    FROM Passenger p
    JOIN Reservation r ON p.PassengerName = r.PassengerName;
    
Query-6:  List Flights by a Specific Crew Member:

     SELECT f.FlightNumber, f.DepartureAirport, f.ArrivalAirport,
     f.DepartureDateTime, f.ArrivalDateTime
     FROM Flight f
     JOIN FlightCrew fc ON f.FlightNumber = fc.FlightNumber
     JOIN Crew c ON fc.CrewID = c.CrewID
     WHERE c.CrewName = 'Paul Roberts';
    
Query-7:  We can count the total number of passengers by loyalty status:

    SELECT LoyaltyStatus, COUNT(*) AS TotalPassengers
    FROM Passenger
    GROUP BY LoyaltyStatus;
   
Query-8:  To count reservations by fare class, we use the following query:

    SELECT FareClass, COUNT(*) AS TotalReservations
    FROM Reservation
    GROUP BY FareClass;
   
