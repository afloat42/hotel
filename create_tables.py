# create_tables.py
# France Cheong
# 14/09/2021
# ###########
# 1. Libraries
# ###########
import sqlite3
# ###########
# 2. Constants
# ###########
DATABASE_URI = "hotel.db"
# For AUTOINCREMENTED PK (whether implied or not)
# Must provide a value of the PK (unlike SQLAlchemy which does not require one)
# If the value is None, it will be autoincremented from the last one inserted
# However, if a value is specified, that value will be inserted

HOTEL_SQL = """
    CREATE TABLE hotel(
    hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    phonenumber VARCHAR(20) NOT NULL,
    address VARCHAR(50) NOT NULL,
    postcode VARCHAR(4),
    city VARCHAR(20) NOT NULL
    )
"""

ROOM_SQL = """
    CREATE TABLE room(
    room_no INTEGER PRIMARY KEY AUTOINCREMENT,
    Occupancy VARCHAR(20) NOT NULL,
    room_type VARCHAR(20) NOT NULL,
    booking_no INTEGER NOT NULL,
    hotel_id INTEGER NOT NULL,
    FOREIGN KEY(hotel_id) REFERENCES hotel(hotel_id),
    FOREIGN KEY(room_type) REFERENCES roomtype(room_type),
    FOREIGN KEY(booking_no) REFERENCES booking(booking_no)
    )
"""

ROOMTYPE_SQL = """
    CREATE TABLE roomtype(
    room_type VARCHAR(20) PRIMARY KEY,
    room_price INTEGER NOT NULL,
    room_desc VARCHAR(50) NOT NULL
    )
"""

EMPLOYEES_SQL = """
    CREATE TABLE employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    phonenumber VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    dob VARCHAR(20) NOT NULL,
    hotel_id INTEGER NOT NULL,
    FOREIGN KEY(hotel_id) REFERENCES hotel(hotel_id)
    )
"""

BOOKING_SQL = """
    CREATE TABLE booking(
    booking_no INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_date VARCHAR(20) NOT NULL,
    guestname varchar(20) not null,
    arrivaldate VARCHAR(20) NOT NULL,
    departuredate VARCHAR(20) NOT NULL,
    numadult INTEGER NOT NULL,
    numchildren INTEGER NOT NULL,
    numinfants INTEGER NOT NULL,
    room_no INTEGER NOT NULL,
    guest_no INTEGER NOT NULL,
    FOREIGN KEY(room_no) REFERENCES room(room_no),
    FOREIGN KEY(guest_no) REFERENCES hotel(guest)
    )
"""

GUEST_SQL = """
    CREATE TABLE guest(
    guest_no INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    phonenumber VARCHAR(20) NOT NULL,
    dob VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    postcode VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    passportno INTEGER NOT NULL,
    creditcard_no VARCHAR(20) NOT NULL,
    card_expiry VARCHAR(10) NOT NULL,
    card_name VARCHAR(20)
    )
"""

"""
Please note that SQLite does not enforce foreign key constraints by default
To enable it, need to execute the following command after you connect to the
database
PRAGMA foreign_keys = 1
e.g.
conn=sqlite3.connect("yourdatabase.db")
conn.execute("PRAGMA foreign_keys = 1")
cur=conn.cursor()
"""
# ###########
# 3. Functions
# ###########
# ###########
# 4. Main method
# ###########
if __name__ == '__main__':
  print("Creating the database and tables")
  print("Please ensure that you've deleted hotel_system.db in the currect folder")
print()
input("Press Enter to continue or Ctrl+C to cancel ...")
# Open a connection
conn = sqlite3.connect(DATABASE_URI)
print(f"Opened a connection to database {DATABASE_URI}")
with conn:
# Get a cursor
  cur = conn.cursor()
print("Got a cursor to the connection")
# 1. Create the Hotel table
cur.execute(HOTEL_SQL)
print(f"Hotel table created in database {DATABASE_URI}")
# 2. Create the room table
cur.execute(ROOM_SQL)
print(f"Room table created in database {DATABASE_URI}")
# 3. Create the room type table
cur.execute(ROOMTYPE_SQL)
print(f"Room Type table created in database {DATABASE_URI}")
# 4. Create the Employee table
cur.execute(EMPLOYEES_SQL)
print(f"Employee table created in database {DATABASE_URI}")
# 5. Create the booking table
cur.execute(BOOKING_SQL)
print(f"Booking table created in database {DATABASE_URI}")
# 6. Create the guest table
cur.execute(GUEST_SQL)
print(f"Guest table created in database {DATABASE_URI}")

print("\nAll done!")
print("\nPlease use DB Browser for SQLite to check the database!")
