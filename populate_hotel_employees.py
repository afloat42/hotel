# poplulate hotel_employee.py
# Sohil Pachbhaiya
#25/04/2023

# 1. Libraries 

import sqlite3

# 2. Constants

DATABASE_URI = "hotel.db"

#3. Functions

def populate_hotel(cur):
    #list of hotel
    hotels = [
        {
        "hotel_id" : None,
        "name"     : "Antique Hotel and Spa (AHS) ",
        "phonenumber" : "04 2283 4246",
        "address"   : "North St & Vincent St N",
        "postcode"  : "3460",
        "city"      : "Daylesford"  
        }
    ]
    sql = "INSERT INTO hotel VALUES (?, ?, ?, ?, ?, ?)" # 6 values for hotel in hotels
    for hotel in hotels:
        print(f"\nInserting: {hotels}")
        param_tuple = [value for value in hotel.values()] # can't use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)
def populate_roomtype(cur):
    #list of room tupe
    #owner would like to add more room type in the future
    roomtypes =[
        {
        "room_type" : "King size room",
        "room_price": 250,
        "room_desc" : "1 king bed and 1 bathroom. if there is children, a portable bed is added to the room and there is an extra change"
        }
    ]
    sql = "INSERT INTO roomtype VALUES (?, ?, ?)" # 3 values for roomtype in roomtypes
    for roomtype in roomtypes:
        print(f"\nInserting: {roomtypes}")
        param_tuple = [value for value in roomtype.values()] # can't use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)

def populate_guest(cur):
    #List of guest
    guests = [
        {
        "guest_no"  : None,
        "last_name" : "Rai",
        "first_name": "Aman",
        "phonenumber": "04 6034 5233",
        "dob"       : "21/05/2000",
        "email"     : "aman.rai@gmail.com",
        "address"   : "12 wallum court",
        "postcode"  : "2484",
        "city"      : "Tomewin",
        "country"   : "Australia",
        "passportno": "04427573",
        "creditcard_no": "1234 5678 9123",
        "card_expiry"   : "12/24",
        "card_name"     : "Aman Rai"
        },
        {
        "guest_no"  : None,
        "last_name" : "holland",
        "first_name": "Tom",
        "phonenumber": "04 8492 5251",
        "dob"       : "17/06/1995",
        "email"     : "tom.holland@gmail.com",
        "address"   : "25 Muscat Street",
        "postcode"  : "6466",
        "city"      : "Cadoux",
        "country"   : "Australia",
        "passportno": "89716767",
        "creditcard_no": "9123 5678 1234 ",
        "card_expiry"   : "12/24",
        "card_name"     : "Tom holland"
        }
    ]

    sql = "INSERT INTO guest VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" # 14 values for roomtype in roomtypes
    for guest in guests:
        print(f"\nInserting: {guests}")
        param_tuple = [value for value in guest.values()] # can't use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)

def populate_employee(cur):
    #list of employees
    #hotel_id will always be a 1 as they all work in AHS
    #it will only change if the owner expands and have more employees
    employees = [
        {
        "employee_id"   : None,
        "last_name"     : "rana",
        "first_name"    : "Anmol",
        "phonenumber"   : "04 8781 7295",
        "email"         : "anmol.rana@gmail.com",
        "address"       : "86 Chatsworth Drive",
        "dob"           : " 20/04/2002",
        "hotel_id"      : 1
        },
        {
        "employee_id"   : None,
        "last_name"     : "Smith",
        "first_name"    : "Jhon",
        "phonenumber"   : "04 2619 9178",
        "email"         : "jhon.smith@gmail.com",
        "address"       : "27 Thyme Avenue",
        "dob"           : "12/09/1990",
        "hotel_id"      : 1
        }
    ]

    sql = "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?)" # 8 values for employee in rmployees
    for employee in employees:
        print(f"\nInserting: {employees}")
        param_tuple = [value for value in employee.values()] # can't use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)

def populate_room(cur):
    #list of room
    #depending the the number of booking, it will affect if the room occupancy is booked or vacant
    #hotel_id will always be 1 as they only have AHS
    rooms= [
        {
        "room_no"   : None,
        "occupancy" : "booked",
        "roomtype"  : "King size room",
        "booking_no": 1,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "booked",
        "roomtype"  : "King size room",
        "booking_no": 2,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        },
        {
        "room_no"   : None,
        "occupancy" : "vacnat",
        "roomtype"  : "King size room",
        "booking_no": 0,
        "hotel_no"  : 1
        }
    ]

    sql = "INSERT INTO room VALUES (?, ?, ?, ?, ?)" # 5 values for employee in rmployees
    for room in rooms:
        print(f"\nInserting: {rooms}")
        param_tuple = [value for value in room.values()] # can't use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)

def populate_booking(cur):
    bookings = [
        {
        "booking_no" : None,
        "booking_date": "15/03/2023",
        "guestname"   : "Rai",
        "arrivaldate" : " 25/04/2023",
        "departuredate": "31/04/2023",
        "numadult"      : "2",
        "numchildren"   : "1",
        "numinfants"    : "0",
        "room_no"       : 1,
        "guest_no"      :1
        },
        {
        "booking_no" : None,
        "booking_date": "10/03/2023",
        "guestname"   : "holland",
        "arrivaldate" : " 25/04/2023",
        "departuredate": "10/05/2023",
        "numadult"      : "2",
        "numchildren"   : "",
        "numinfants"    : "0",
        "room_no"       : 2,
        "guest_no"      :2
        }
    ]

    sql = "INSERT INTO booking VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" # 10 values for employee in rmployees
    for booking in bookings:
        print(f"\nInserting: {bookings}")
        param_tuple = [value for value in booking.values()] # can't use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)



if __name__ == '__main__':

    print("\nPopulating hotel database  ....") 

    input("\nPress Enter to continue or Ctrl+C to cancel ...")

    with sqlite3.connect(DATABASE_URI) as conn:
        print(f"Opened a connection to database {DATABASE_URI}")

        # 1. Get a cursor
        cur = conn.cursor()
        print("Got a cursor to the connection")

        # 2. Populate hotel
        populate_hotel(cur)
        print(f"Hotel table populated in database {DATABASE_URI}")

        #3. Populate roomtype
        populate_roomtype(cur)
        print(f"roomtype table populated in database {DATABASE_URI}")

        #4. Populate roomtype
        populate_guest(cur)
        print(f"guest table populated in database {DATABASE_URI}")

        #5. Populate employee
        populate_employee(cur)
        print(f"employee table populated in database {DATABASE_URI}")

        #6. Populate room
        populate_room(cur)
        print(f"room table populated in database {DATABASE_URI}")

        #7. Populate roomtype
        populate_booking(cur)
        print(f"booking table populated in database {DATABASE_URI}")

        # 3. Save the records
        conn.commit()

        # No need to close the cursor and connection when using the with statement
        # Will be closed automatically

    print("\nAll done!")    

    print("\nPlease use DB Browser for SQLite to check the database!")                
