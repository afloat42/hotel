#employee_dao_test.py
#sohil pachbhaiya
# 25/04/2023

"""
The code is this file is implemented as procedural code i.e. no OOP

The test is best done on an empty database as the appt_id used is 1
And it can be run more than once.
"""

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from booking_dao import BookingDAO

'''
Test the create() method of the BookingDAO class
'''

from booking_dao import BookingDAO


def test_create():
    """
    Test the create() method of the BookingDAO class.
    """
    print("\n1. Test create a booking ...")

    booking_dao = BookingDAO()

    # Setup the data as a dictionary
    # Note: USE YOUR OWN DATA FOR TESTING
    """
    data = {}
    #data['booking_no'] = "" # No - do not pass any value for employee_id
    data['booking_date'] = "15/05/2023"
    data['first_name'] = "jake"
    data['arrivaldate'] = "30/05/2023"
    data['departuredate'] = "07/06/2023"
    data['numadult'] = "2"
    data['numchildren'] = "0"
    data['numinfants'] = "0"
    data['room_no'] = "3"
    data['guest_no'] = 3

    """

    data = {
        'booking_date': "15/05/2023",
        'guestname': "jake",
        'arrivaldate': "30/05/2023",
        'departuredate': "07/06/2023",
        'numadult': "2",
        'numchildren': "0",
        'numinfants': 1,
        'room_no': 3,
        'guest_no': 3,
    }

    result = booking_dao.create(data)

    print(result)


def test_find_by_nos():
    """
    Test the find_by_nos() method of the BookingDAO class.
    """
    print("\n2. Test find by booking_no ...")

    booking_dao = BookingDAO()

    booking_no = 1

    result = booking_dao.find_by_nos(booking_no)

    print(result)


def test_find_all():
    """
    Test the find_all() method of the BookingDAO class.
    """
    print("\n3. Test find all bookings ...")

    booking_dao = BookingDAO()

    result = booking_dao.find_all()

    print(result)


def test_find_by_booking_date():
    """
    Test the find_by_booking_date() method of the BookingDAO class.
    """
    print("\n4. Test find by booking date ...")

    booking_dao = BookingDAO()

    booking_date = "15/05/2023"

    result = booking_dao.find_by_booking_date(booking_date)

    print(result)


def test_find_no():
    """
    Test the find_no() method of the BookingDAO class.
    """
    print("\n5. Test find booking numbers ...")

    booking_dao = BookingDAO()

    result = booking_dao.find_no()

    print(result)


def test_update():
    """
    Test the update() method of the BookingDAO class.
    """
    print("\n6. Test update a booking ...")

    booking_dao = BookingDAO()

    booking_no = 1

    data = {
        'booking_date': "12/05/2023",
        'guestname': "bill",
        'phonenumber': "04 8142 8924",
        'arrivaldate': "15/05/2023",
        'departuredate': "20/05/2023",
        'numadult': "1",
        'numchildren': "0",
        'numinfants': "1",
        'room_no': 3,
        'guest_no': 3
    }

    # Call the update() method from the DAO
    # and pass the employee_id and data as parameters
    result = booking_dao.update(booking_no, data)

    print(result)

def test_delete():
    print("\n7. Test delete a employee ...")

    booking_dao = BookingDAO()

    # Assign an employee_id
    booking_no = 1 # exists

    # Call the delete() method from the DAO
    # and pass the employee_id as parameter - could pass it directly
    result = booking_dao.delete(BookingDAO)

    print(result)


if __name__ == "__main__":
    print("\nTesting employee DAO ...")
    print("Please ensure that you perform the tests on a blank database ...")
    print("First delete 'hotel_system.db' then run 'python create_tables.py' to create a blank database")

    print()
    input("Press Enter to continue or Ctrl+C to cancel ...")

    # 1. Test create method from appointment_dao.py
    test_create()

    # 2. Test find by id method from appointment_dao.py
    test_find_by_nos()

    # 3. Test find all method from appointment_dao.py
    test_find_all()

    # 4. Test find by date method from appointment_dao.py
    test_find_by_booking_date()

    # 5. Test find ids method from appointment_dao.py
    test_find_no()

    # 6. Test update method from appointment_dao.py
    test_update()

    # 7. Test delete method from appointment_dao.py
    test_delete()

    print("\nAll done!")

    print("\nPlease use DB Browser for SQLite to check the database!")




