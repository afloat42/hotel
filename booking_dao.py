# guest_dao_test.py
# Sohil Pachbhaiya
# 5/2/2023
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = 'hotel.db'

class BookingDAO():

    def create(self, data):

        # Print info for debugging
        print("\nCreating a Booking ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Using Parameterized Query i.e. question marks as placeholders for the actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO booking VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);" # guest table has 10 attributes
            param_tuple = (
                None, # booking_no is set to None for database to autoincrement
                data['booking_date'], 
                data['guestname'],  
                data['arrivaldate'], 
                data['departuredate'],
                data['numadult'],
                data['numchildren'],
                data['numinfants'],
                data['room_no'],
                data['guest_no']
                )
            cur.execute(query, param_tuple)
            result['message'] = 'booking added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_booking_no = cur.lastrowid
            print(f"inserted_booking_no: {inserted_booking_no}")
            result['booking_no'] = inserted_booking_no

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create booking failed!' 
            print(f"Database {DATABASE_URI} - Create booking failed!")
            print(error)
        finally:
            # The finally block is always executed - even if an exception happened
            # This is the ideal place to close the connection
            # It's always a good idea to check if the object exists before calling a method/function from the object
            # Invoking a method on object which does not exist will cause your code to crash
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary  

    def find_by_nos(self, booking_no):

        # Print info for debugging
        print("\nFinding a booking ...\n")
        print(f"booking_no: {booking_no}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM booking WHERE booking_no=?;"
            #param_tuple = (booking_no) # Does not work as it's converted to an int, need the comma at the end
            param_tuple = (booking_no, ) # Works as this is a tuple of length 1
            cur.execute(query, param_tuple)
            row = cur.fetchone() # get the next row - there would be just one row returned by the database
            if row:
                # cursor.description contains the name of the columns
                # Use dictionary compejension to build the dictionary
                # Use list comprehension to get the list of column names from cursor.description
                # The column name is at index 0 i.e. the first position
                col_names = [description[0] for description in cur.description]
                #print(f"Column names: {col_names}")
                # Using dictionary comprehension and enumerate() to match the column names with their index positions
                b = {key: row[i] for i, key in enumerate(col_names)} # works
                result['guest'] = b
            else:    
                result['message'] = "Booking not found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by No failed!' 
            print(f"Database {DATABASE_URI} - Find by No failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        #print(f"result: {result}")
        return result # return the result as a dictionary

    def find_by_booking_date(self, booking_date): 

        # Print info for debugging
        print("\nFinding guest by last_name ...\n")
        print(f"last_name: {booking_date}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            #query = "SELECT * FROM guest WHERE last_name LIKE ?" # Partial match
            query = "SELECT * FROM booking WHERE booking_date = ?;" # exact match
            param_tuple = (booking_date, )
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['guest'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one hotel - so create a list
                list_booking= [] # Create an empty list to append doctor dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary compejension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    b = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_booking.append(b) # Append the doctor dict to the doctor list
                      
                # Store the doctor list in the result dict under key "doctors"              
                result['booking'] = list_booking              

            else:    
                result['message'] = "No booking found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by booking_date failed!' 
            print(f"Database {DATABASE_URI} - Find by booking_date failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):

        # Print info for debugging
        print("\nFinding all booking_no ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM booking;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['doctors'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one hotel - so create a list
                list_booking = [] # Create an empty list to append hotel dicts
                for x in rows: # rows is a list of SQLite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary comprehension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    b = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_booking.append(b) # Append the doctor dict to the doctor list
                    pass     

                # After the for loop
                # Store the doctoe list in the result dict under key "doctors" - PLURAL             
                result['booking'] = list_booking    
            else:    
                result['message'] = "No booking found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find all failed!' 
            print(f"Database {DATABASE_URI} - Find all failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")    
        return result # return the result as a dictionary


    def find_no(self):
        """
        This is a special method similar to find_all but returns doc_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all booking no ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT guest_no FROM booking;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['booking_no'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No booking no found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find no failed!' 
            print(f"Database {DATABASE_URI} - Find no failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}") 
        return result # return the result as a dictionary

    def update(self, booking_no, data):

        # Print info for debugging
        print("\nUpdating booking ...\n")
        print(f"booking_no: {booking_no}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in doctor table except doc_id
            query = """UPDATE booking
               SET 
                  booking_date=?,
                  guestname=?,
                  arrivaldate=?,
                  departuredate=?,
                  numadult=?,
                  numchildren=?, 
                  numinfants=?, 
                  room_no=?, 
                  guest_no=?

               WHERE 
                  booking_no = ?;"""
            
            param_tuple = (
                data['booking_date'], 
                data['guestname'],
                data['arrivaldate'],
                data['departuredate'], 
                data['numadult'], 
                data['numchildren'], 
                data['numinfants'],
                data['room_no'],
                data['guest_no'],
                booking_no)
            cur.execute(query, param_tuple)
            result['message'] = 'booking Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'booking NOT updated!' 
            print(f"Database {DATABASE_URI} - Update booking failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, booking_no):

        # Print info for debugging
        print("\nDeleting booking ...\n")
        print(f"booking_no: {booking_no}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "DELETE FROM booking WHERE booking_no = ?;"
            param_tuple = (booking_no, )
            cur.execute(query, param_tuple)
            result['message'] = 'Booking deleted!'
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Booking NOT deleted!'
            print(f"Database {DATABASE_URI} - Delete booking failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary