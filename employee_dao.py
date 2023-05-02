#employee_dao.py
#Sohil Pachbhaiya
#25/04/2023

# Import packages
import sqlite3

# Constants
DATABASE_URI = 'hotel.db'

class EmployeeDAO():
    def create(self, data):

        # Print info for debugging
        print("\nCreating an employee ...\n")
        print(f"data: {data}")

        result = {}

        # Using Parameterized Query i.e. question marks as placeholders for the actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?);" # appointment table has 8 attributes
            param_tuple = (
                None, # employee_id is set to None for database to autoincrement
                data['last_name'],
                data['first_name'],
                data['phonenumber'],
                data['email'],
                data['address'],
                data['dob'],
                data['hotel_id'])
            cur.execute(query, param_tuple)
            result['message'] = 'Employee added successfully!'

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_employee_id = cur.lastrowid
            print(f"inserted_employee_id: {inserted_employee_id}")
            result['employee_id'] = inserted_employee_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create employee failed!'
            print(f"Database {DATABASE_URI} - Create employee failed!")
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


    def find_by_id(self,employee_id):
        # Print info for debugging
        print("\nFinding an employee ...\n")
        print(f"employee_id: {employee_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM employees WHERE employee_id=?;"
            param_tuple = (employee_id, ) # Works as this is a tuple of length 1
            cur.execute(query, param_tuple)
            row = cur.fetchone() # get the next row - there would be just one row returned by the database
            if row:
                # cursor.description contains the name of the columns
                # Use dictionary compejension to build the dictionary
                # Use list comprehension to get the list of column names from cursor.description
                # The column name is at index 0 i.e. the first position
                col_names = [description[0] for description in cur.description]
                # Using dictionary comprehension and enumerate() to match the column names with their index positions
                e = {key: row[i] for i, key in enumerate(col_names)}
                result['employees'] = e
            else:
                result['message'] = "Employee not found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by id failed!'
            print(f"Database {DATABASE_URI} - Find by id failed!")
            print(error)
        finally:
            if conn:
                conn.close()

        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        return result # return the result as a dictionary
    
    def find_by_dob(self, dob):

        # Print info for debugging
        print("\nFinding employee(s) by dob ...\n")
        print(f"dob: {dob}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            #query = "SELECT * FROM employee WHERE dob LIKE ?" # Partial match
            query = "SELECT * FROM employees WHERE dob = ?;" # exact match
            param_tuple = (dob, )
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['employee'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one appointments - so create a list
                list_employees = [] # Create an empty list to append appointment dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary compejension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    e = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_employees.append(e) # Append the appointment dict to the appointment list

                # Store the appointment list in the result dict under key "appointments"
                result['appointments'] = list_employees

            else:
                result['message'] = "No appointments found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by dob failed!'
            print(f"Database {DATABASE_URI} - Find by dob failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}") 
        return result  # return the result as a dictionary


    def find_all(self):
        # Print info for debugging
        print("\nFinding all employees ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM employees;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['doctors'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one employee - so create a list
                list_employees = [] # Create an empty list to append employee dicts
                for x in rows: # rows is a list of SQLite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary comprehension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    e = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_employees.append(e) # Append the employee dict to the appointment list
                    pass

                # After the for loop
                # Store the appointment list in the result dict under key "appointments" - PLURAL
                result['employee'] = list_employees
            else:
                result['message'] = "No employee found!"
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
        This is a special method similar to find_all but returns employee_id only,
        not the full details
        """
        # Print info for debugging
        print("\nFinding all employees ids ...\n")

        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT employee_id FROM employees;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['employee_id'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:
                result['message'] = "No employees found!"
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
    

    def update(self, employee_id, data):

        # Print info for debugging
        print("\nUpdating employee ...\n")
        print(f"employee_id: {employee_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in employee table except employee_id
            query = """UPDATE employees
            SET
              last_name=?,
              first_name=?,
              phonenumber=?,
              email=?,
              address=?,
              dob=?,
              hotel_id=?
            WHERE
              employee_id = ?;
            """
            param_tuple = (
                data['last_name'],
                data['first_name'],
                data['phonenumber'],
                data['email'],
                data['address'],
                data['dob'],
                data['hotel_id'],
                employee_id)
            cur.execute(query, param_tuple)
            result['message'] = 'Employees updated!'
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Employees NOT updated!'
            print(f"Database {DATABASE_URI} - Update appointment failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        return result
    
    def delete(self, employee_id):

        # Print info for debugging
        print("\nDeleting employee ...\n")
        print(f"employee_id: {employee_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "DELETE FROM employees WHERE employee_id = ?;"
            param_tuple = (employee_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'Employee deleted!'
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Employee NOT deleted!'
            print(f"Database {DATABASE_URI} - Delete employee failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary


