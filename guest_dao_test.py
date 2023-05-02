# guest_dao_test.py
# Sohil Pachbhaiya
# 5/2/2023

"""
The code is this file is implemented as procedural code i.e. no OOP

The test is best done on an empty database as the doc_id used is 1
And it can be run more than once
"""

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from guest_dao import GuestDAO

'''
Test the create() method of the GuestDAO class
'''
def test_create():

    # Print info for debugging
    print("\n1. Test create a guest ...") #\n means print("\n") a blank line    
        
    # Instantiate the doctor DAO
    guest_dao = GuestDAO()

    # Setup the data as a dictionary
    # Note: USE YOUR OWN DATA FOR TESTING
    """
    data = {}
    #data['guest_no'] = "" # No - do not pass any value for guest_no
    data['last_name'] = "rai"
    data['first_name'] = "tom"
    data['phonenumber'] = "0416673315"
    data['dob'] = "21/03/2000"
    data['email'] = "tom.rai@gmail.com"
    data['address'] = "27 edmondshaw drive"
    data['postcode'] = "3000"
    data['city'] = "melbourne"
    data['country'] = "singapore"
    data['passportno'] = "90901232"
    data['creditcard_no'] = "90901232"
    data['card_expiry'] = "90901232"
    data['card_name'] = "90901232"
    """

    # Alternatively, the data could be set up in JSON format
    # Do not pass any value for guest_no
    data = {
        'last_name':"rai",
        'first_name':"tom",
        'phonenumber': "0416673315",
        'dob': "21/03/2000",
        'email': "tom.rai@gmail.com",
        'address'   : "27 edmondshaw drive",
        'postcode'  : "3000",
        'city'   :"melbourne",
        'country': "singapore",
        'passportno': "90901232",
        'creditcard_no': "1234 5678 9123",
        'card_expiry': "12/24",
        'card_name': "tom rai"# no comma on last item
    }

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = guest_dao.create(data)

    # Print the result
    print(result)


def test_find_by_nos():

    # Print info for debugging
    print("\n2. Test find by no ...")   
   
    # Instantiate the doctor DAO
    guest_dao = GuestDAO()

    # Assign an doc_id
    guest_no = 1 # exists
    #doc_id = 2 # does not exist?
    
    result = guest_dao.find_by_nos(guest_no)

    # Print the result
    print(result)
    

def test_find_all():

    # Print info for debugging
    print("\n3. Test find all ...")   
   
    # Instantiate the doctor DAO
    guest_dao = GuestDAO()

    result = guest_dao.find_all()

    # Print the result
    print(result)

 
def test_find_by_last_name():

    # Print info for debugging
    print("\n4. Test find by last_name  ...")   
        
    # Instantiate the doctor DAO    
    guest_dao = GuestDAO()
      
    # Assign a lastname  
    last_name = "rai" # exists
    #lastname = "xyz" # does not exist

    result = guest_dao.find_by_last_name(last_name)

    # Print the result
    print(result)

def test_find_no():

    # Print info for debugging
    print("\n5. Test find nos ...")   

    # Instantiate the doctor DAO
    guest_dao = GuestDAO()

    # Call the find_ids() method from the DAO
    result = guest_dao.find_no()

    # Print the result
    print(result)


def test_update():

    # Print info for debugging
    print("\n6. Test update guest ...")   

    # Instantiate the doctor DAO
    guest_dao = GuestDAO()

    # Assign an doc_id 
    guest_no = 1 # exists
    #doc_id = 2 # does not exist?

    # Create a dictionary and add items
    # Do not add the doc_id to the dict
    data = {}
    data['last_name'] = "thapa"
    data['first_name'] = "sohil"
    data['phonenumber'] = "16673315"
    data['dob'] = "24/09/2001"
    data['email'] = "sohil.thapa@gmail.com"
    data['address'] = "30 edmondshaw drive"
    data['postcode'] = "3000"
    data['city'] = "deer park"
    data['country'] = "melbourne"
    data['passportno'] = "21244322"
    data['creditcard_no'] = "1234 5678 9123"
    data['card_expiry'] = "12/24"
    data['card_name'] = "sohil thapa"
        
    # Call the update() method from the DAO
    # and pass the doc_id and data as parameters    
    result = guest_dao.update(guest_no, data)

    # Print the result
    print(result)


def test_delete():

    #Print info for debugging
    print("\n7. Test delete a hotel ...")   

    guest_dao = GuestDAO()

    # Assign an hotel_id
    guest_no = 1 # exists
    #doc_id = 2 # does not exist?

    # Call the delete() method from the DAO
    # and pass the doc_id as parameter - could pass it directly
    result = guest_dao.delete(guest_no)

    # Print the result
    print(result)


if __name__ == "__main__":

    # You may wish to comment/uncomment the functions calls below
    # To select which ones to run or not to run

    # If you run test_create() twice in a row
    # You will try to insert the same record twice
    # You Will get an integrity error
    # Phone number has to be unique
    # Either comment out test_create() (to run the other function calls)
    # Or use DB Browser for SQLite to delete the record

    # You may want to run test_delete() last
    # Because if you delete the record as soon as you insert
    # You cannot run the other tests like test_find_by_id(), test_update()

    # Use DB Browser for SQLite to check if data was really inserted/updated/deleted

    # If the database is opened in DB Browser for SQLite, 
    # you might not run the tests as the database will be locked
    # Need to close the database in DB Browser for SQLite

    print("\nTesting Doctor DAO ...")
    print("Please ensure that you perform the tests on a blank database ...")
    print("First delete 'hotel_system.db' then run 'python create_tables.py' to create a blank database")

    print()
    input("Press Enter to continue or Ctrl+C to cancel ...")

    # 1. Test create method from guest_dao.py
    test_create()

    # 2. Test find no method from guest_dao.py
    test_find_by_nos()

    # 3. Test find all method from guest_dao.py
    test_find_all()

    # 4. Test find by lastname method from guest_dao.py
    test_find_by_last_name()
    
    # 5. Test find by no method from guest_dao.py
    test_find_no()

    # 6. Test update method from guest_dao.py
    test_update()

    # 7. Test delete method from guest_dao.py
    test_delete()

    print("\nAll done!") 

    print("\nPlease use DB Browser for SQLite to check the database!") 