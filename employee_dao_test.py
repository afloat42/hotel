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
from employee_dao import EmployeeDAO

'''
Test the create() method of the EmployeeDAO class
'''

def test_create():
    # Print info for debugging
    print("\n1. Test create a employee ...") #\n means print("\n") a blank line

    # Instantiate the appointment DAO
    employee_dao = EmployeeDAO()

    # Setup the data as a dictionary
    # Note: USE YOUR OWN DATA FOR TESTING
    """
    data = {}
    #data['employee_id'] = "" # No - do not pass any value for employee_id
    data['last_name'] = "hill"
    data['first_name'] = "jake"
    data['phonenumber'] = "04 7123 8141"
    data['email'] = "jake.hill@gmail.com"
    data['address'] = "27 edmondshaw drive"
    data['dob'] = "15/09/2000"
    data['hotel_id'] = 1

    """

    # Alternatively, the data could be set up in JSON format
    # Do not pass any value for appt_id
    data = {
        'last_name': "hill",
        'first_name': "jake",
        'phonenumber': "04 7123 8141",
        'email': "jake.hill@gmail.com",
        'address': "27 edmondshaw drive",
        'dob': "15/09/2000",
        'hotel_id': 1 # no comma on last item
    }

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = employee_dao.create(data)

    # Print the result
    print(result)

def test_find_by_id():
    print("\n2. Test find by id ...")

    # Instantiate the employee DAO
    employee_dao = EmployeeDAO()

    # Assign an appt_id
    employee_id = 1 # exists

    result = employee_dao.find_by_id(employee_id)

    print(result)

def test_find_all():
    print("\n3. Test find all ...")

    # Instantiate the employee DAO
    employee_dao = EmployeeDAO()

    result = employee_dao.find_all()

    print(result)

def test_find_by_dob():
    print("\n4. Test find by dob  ...")

    # Instantiate the employee DAO
    employee_dao = EmployeeDAO()

    # Assign a date
    dob = "12/09/1990" # exists
    #lastname = "212/09/1990" # does not exist

    result = employee_dao.find_by_dob(dob)

    print(result)

def test_find_ids():
    print("\n5. Test find ids ...")

    # Instantiate the employee DAO
    employee_dao = EmployeeDAO()

    # Call the find_ids() method from the DAO
    result = employee_dao.find_ids()

    # Print the result
    print(result)

def test_update():
    print("\n6. Test update employee ...")

    # Instantiate the appointment DAO
    employee_dao = EmployeeDAO()

    # Assign an appt_id
    employee_id = 1 # exists

    # Create a dictionary and add items
    # Do not add the employee_id to the dict
    data = {}
    data['last_name'] = "baus"
    data['first_name'] = "bill"
    data['phonenumber'] = "04 8142 8924"
    data['email'] = "bill.baus@gmail.com"
    data['address'] = "62 edmondshaw lane"
    data['dob'] = "12/02/1999"
    data['hotel_id'] = 1

    # Call the update() method from the DAO
    # and pass the employee_id and data as parameters
    result = employee_dao.update(employee_id, data)

    print(result)

def test_delete():
    print("\n7. Test delete a employee ...")

    employee_dao = EmployeeDAO()

    # Assign an employee_id
    employee_id = 1 # exists

    # Call the delete() method from the DAO
    # and pass the employee_id as parameter - could pass it directly
    result = employee_dao.delete(employee_id)

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
    test_find_by_id()

    # 3. Test find all method from appointment_dao.py
    test_find_all()

    # 4. Test find by date method from appointment_dao.py
    test_find_by_dob()

    # 5. Test find ids method from appointment_dao.py
    test_find_ids()

    # 6. Test update method from appointment_dao.py
    test_update()

    # 7. Test delete method from appointment_dao.py
    test_delete()

    print("\nAll done!")

    print("\nPlease use DB Browser for SQLite to check the database!")




