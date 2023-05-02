# doctor_dao.py
# France Cheong
# 11/10/2021
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = 'hotel.db'

class HotelDAO():

    def create(self, data):

        # Print info for debugging
        print("\nCreating a Hotel ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Using Parameterized Query i.e. question marks as placeholders for the actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO doctor VALUES (?, ?, ?, ?, ?, ?);" # hotel table has 6 attributes
            param_tuple = (
                None, # hotel_id is set to None for database to autoincrement
                data['name'], 
                data['phonenumber'],  
                data['address'], 
                data['postcode'],
                data['city'])
            cur.execute(query, param_tuple)
            result['message'] = 'hotel added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_hotel_id = cur.lastrowid
            print(f"inserted_hotel_id: {inserted_hotel_id}")
            result['hotel_id'] = inserted_hotel_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create hotel failed!' 
            print(f"Database {DATABASE_URI} - Create hotel failed!")
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

    def find_by_id(self, hotel_id):

        # Print info for debugging
        print("\nFinding a hotel ...\n")
        print(f"hotel_id: {hotel_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM hotel WHERE hotel_id=?;"
            #param_tuple = (hotel_id) # Does not work as it's converted to an int, need the comma at the end
            param_tuple = (hotel_id, ) # Works as this is a tuple of length 1
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
                h = {key: row[i] for i, key in enumerate(col_names)} # works
                result['hotel'] = h
            else:    
                result['message'] = "Hotel not found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by id failed!' 
            print(f"Database {DATABASE_URI} - Find by id failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        #print(f"result: {result}")
        return result # return the result as a dictionary

    def find_by_name(self, name): 

        # Print info for debugging
        print("\nFinding hote(s) by name ...\n")
        print(f"name: {name}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            #query = "SELECT * FROM hotel WHERE name LIKE ?" # Partial match
            query = "SELECT * FROM hotel WHERE name = ?;" # exact match
            param_tuple = (name, )
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['hotel'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one hotel - so create a list
                list_hotels = [] # Create an empty list to append doctor dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary compejension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    h = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_hotels.append(h) # Append the doctor dict to the doctor list
                      
                # Store the doctor list in the result dict under key "doctors"              
                result['hotel'] = list_hotels              

            else:    
                result['message'] = "No hotel found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by name failed!' 
            print(f"Database {DATABASE_URI} - Find by name failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):

        # Print info for debugging
        print("\nFinding all name ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM hotel;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['doctors'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one hotel - so create a list
                list_hotels = [] # Create an empty list to append hotel dicts
                for x in rows: # rows is a list of SQLite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary comprehension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    h = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_hotels.append(h) # Append the doctor dict to the doctor list
                    pass     

                # After the for loop
                # Store the doctoe list in the result dict under key "doctors" - PLURAL             
                result['hotel'] = list_hotels    
            else:    
                result['message'] = "No hotel found!"
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


    def find_ids(self):
        """
        This is a special method similar to find_all but returns doc_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all hotel ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT hotel_id FROM hotel;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['hotel_id'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No hotel found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find ids failed!' 
            print(f"Database {DATABASE_URI} - Find ids failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}") 
        return result # return the result as a dictionary

    def update(self, hotel_id, data):

        # Print info for debugging
        print("\nUpdating hotel ...\n")
        print(f"hotel_id: {hotel_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in doctor table except doc_id
            query = """UPDATE hotel
               SET 
                  name=?, 
                  phonenumber=?, 
                  address=?, 
                  postcode=?,
                  city=?
               WHERE 
                  hotel_id = ?;"""
            param_tuple = (
                data['name'], 
                data['phonenumber'], 
                data['address'], 
                data['postcode'],
                data['city'],
                hotel_id)
            cur.execute(query, param_tuple)
            result['message'] = 'Hotel Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Hotel NOT updated!' 
            print(f"Database {DATABASE_URI} - Update Hotel failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, hotel_id):

        # Print info for debugging
        print("\nDeleting hotel ...\n")
        print(f"hotel_id: {hotel_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "DELETE FROM hotel WHERE hotel_id = ?;"
            param_tuple = (hotel_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'hotel deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'hotel NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete hotel failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    