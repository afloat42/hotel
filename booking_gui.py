# guest_dao_test.py
# Sohil Pachbhaiya
# 5/2/2023

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox

from validation import Validation
from booking_dao import BookingDAO

class EmployeeGUI():
    """GUI class to perform CRUD operations on the doctor table in the database"""

    def __init__(self):
        """Initialiser"""

        # Instantiate a data access object 
        # Contains methods to access the database
        self.booking_dao = BookingDAO

        # Instantiate a calidation object
        # contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.booking_no = tk.StringVar()
        self.booking_date = tk.StringVar()
        self.guestname = tk.StringVar()
        self.arrivaldate = tk.StringVar()
        self.departuredate = tk.StringVar()
        self.numadult = tk.StringVar()
        self.numchildren = tk.StringVar()
        self.numinfants = tk.StringVar()
        self.room_no = tk.StringVar()
        self.guest_no = tk.StringVar()

        # List of employee ids - lb for listbox
        self.lb_id = None

        # Messagebox title
        self.mb_title_bar = "Booking CRUD"

        pass

    def create_gui(self,root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.
        Notice that the "root" window is passed the second parameter in the 
        method header.
        Also notice that the first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """
        # Good practice to print something at the start of the method 
        # e.g. which method is being executed, the values of parameters passes, 
        # etc
        # Good for tracing the execution of the program while debugging it
        # After debugging, you may want to "comment out" some of the 
        # print statements so that they do not execute and print too 
        # much stuff in the console
        print("\nCreating booking gui")

        # employee_frame = tk.Frame(root).pack() 
        # cannot write the above as pack() does not return anything
        # and need the variable name to refer to it elsewhere
        # DO NOT SPECIFY ANY WIDTH AND HEIGHT OF THE FRAMES 
        # HERE FOR FLEXIBILITY REASONS
        # The height and width or the root window can be specified 
        # in the main GUI (or in the main() method)

        booking_frame = tk.Frame(root)
        booking_frame.pack()

        # Add a frame to contain the form widgets
        # To put a number of widgets in a column one on top of the other, 
        # just use pack() without any options
        # Use the fill=tk.X option to make all widgets as wide as the parent widget
        # To pack widgets side by side, use the side option 
        # e.g. side=tk.LEFT, tk.BOTTOM, tk.RIGHT (default is tk.TOP)
        # Use the fill=tk.Y option to make all widgets as tall as the parent widget
        # have also fill=tk.BOTH option
        # The anchor= option is used to position the widget in the container, 
        # default is tk.CENTER
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding arounf widgets: padx= pady=  default is 0
        form_frame = tk.Frame(booking_frame)
        form_frame.pack()

        # row 0:  title label
        # The variable name is not needed
        # By default, the text is centered
        # To right align use anchor=e (east) not justify=RIGHT which is used 
        # for aligning multiple lines
        # Labels have padx= and pady= options but no ipadx= and ipady=
        # Check the ulr above, to finc out more about the many options 
        # available for configuring labels!!!
        # STICK TO THE DEFAULT VALUES,  
        # UNLESS YOU HAVE A GOOD REASON TO CHANGE THEM!!!!!!!!!!!!!!!!
        # For spanning multiple rows and columns, 
        # use rowspan= and columnspan= options (default is 1)
        # Use the sticky= option for positioning 
        # (instead of anchor= as used in pack) - 
        # (default is centered) values are: n, w, e, w, nw, etc
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding around widgets: padx= pady=  default is 0
        # Use the width= option to specify how wide in terms of number of characters

        tk.Label(
            form_frame,
            font=('arial, 10'),
            text = "Booking").grid(row =0, column=0, columnspan=3)
        
        # row 1: guest_no label, guest_no entry and list_of_nos label
        tk.Label(
            form_frame, 
            text= "ooking Number", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=1, column=0)
        # Need to use both padx and pady to leave a vertical space between rows of labels
        # And a space between the  label and its entry field
        # Entry has no padding options
        # Use the width= option to specify how wide in terms of number of characters
        tk.Entry(
            form_frame, 
            textvariable=self.booking_no, 
            width=30, 
            bd=1, 
            state=tk.DISABLED).grid(row=1, column=1)
        # employee_id is disabled to prevent user from entering a value
        # employee_id is generated by the database because AUTOINCREMENT 
        # was specified in the database schema
        tk.Label(
            form_frame, 
            text= "Booking Nos", 
            font=('arial', 10)).grid(row=1, column=2)
        
        # row 2: last_name label, last_name entry and listbox of numbers
        tk.Label(
            form_frame, 
            text= "Booking date", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=2, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.booking_date, 
            width=30, 
            bd=1).grid(row=2, column=1)
        # Use the height= option to specify the height, default is 10
        # Use the width= option to specify the number of characters, default is 20
        self.lb_id = tk.Listbox(form_frame)
        self.lb_id.grid(row=2, column=2, rowspan=5)
        # 'self' means instance attribute rather than local variable
        # since python allows using variables before they are declared
        # it does not matter whether lb_ids has been declared or not at the 
        # top of the file before the methods definition
        # Set the method to be called when an item is clicked on the listbox 
        self.lb_id.bind('<<ListboxSelect>>', self.on_list_select)

        # row 3: first_name label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "guest name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=3, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.guestname, 
            width=30, 
            bd=1).grid(row=3, column=1)
        
        # row 4: phone number label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "arrival date", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=4, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.arrivaldate, 
            width=30, 
            bd=1).grid(row=4, column=1)
        
        # row 5: email label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "depart uredate", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=5, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.departuredate, 
            width=30, 
            bd=1).grid(row=5, column=1)

        # row 6: address label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Address", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=6, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.address, 
            width=30, 
            bd=1).grid(row=6, column=1)
        
        # row 7: dob label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Date of Birth", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=7, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.dob, 
            width=30, 
            bd=1).grid(row=7, column=1)
        # row 8: dob label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Hotel Id", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=8, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.hotel_id, 
            width=30, 
            bd=1).grid(row=8, column=1)
        
        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid with row 
        # and col locations
        # pady to leave a space from frame on top
        button_frame = tk.Frame(employee_frame, pady=10)
        button_frame.pack()
        # Use the anchor= option to position the button
        # External padding around buttons: padx= pady=  default is 0
        # Use the width= option to specify the number of characters, 
        # otherwise calculated based on text width
        tk.Button(
            button_frame, 
            width=10, text="Clear", 
            command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Save", 
            command=self.save).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Delete", 
            command=self.delete).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Load", 
            command=self.load).pack(side=tk.LEFT)
        
        # Return a reference to the high level frame created
        # Will need the reference to be able to destroy it in the calling function
        return employee_frame
    
    def clear_fields(self):
        """Clear the fields of the form"""

        print("\nClearing fields ...")
        # Just blank all the fields
        self.employee_id.set("")
        self.last_name.set("")
        self.first_name.set("")
        self.phonenumber.set("")
        self.email.set("")
        self.address.set("")
        self.dob.set("")
        self.hotel_id.set("")

    def save(self):
        """Save the data displayed on the form to the database."""


        print("\nSaving a employee ...")

        # Get the data
        data = self.get_fields()   
        #no validation
        """
        if (len(data['employee_id'])==0):
            print("Calling create() as employee_id is absent")
            self.create(data)
        else:
            print("Calling update() as employee_id is present")
            self.update(data) 
        """
        
        
        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['employee_id'])==0):
                # If nothing has been entered in guest_no 
                # i.e. its length is zero characters
                print("Calling create() as employee_id is absent")
                self.create(data)
            else:
                print("Calling update() as employee_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass 
            
    def get_fields(self):
        """Get the data entered in the fields of the form"""

        print("\nGetting fields ...")

        employee = {}
        # employee_id is ignored when creating a record
        employee['employee_id'] = self.employee_id.get()
        employee['last_name'] = self.last_name.get()
        employee['first_name'] = self.first_name.get()
        employee['phonenumber'] = self.phonenumber.get()
        employee['email'] = self.email.get()
        employee['address'] = self.address.get()
        employee['dob'] = self.dob.get()
        employee['hotel_id'] = self.hotel_id.get()

        print(f"employee: {employee}")

        return employee
    
    def create(self, data):
        """
        Create a new record in the database.
        A messagebox is used display the outcome (success or failure) 
        of the create operation to the user.

        Parameters (apart from self):
            data: dictionary object containing doctor data to be saved
 
        Return: name
        """

        print("\nCreating a employee ...")
        print(f"data: {data}")
        employee_dao = EmployeeDAO()
        result = employee_dao.create(data)
        messagebox.showinfo(self.mb_title_bar, result)


        pass

    def update(self, data):
        """Update a record in the database"""

        print("\nUpdating a employee ...")
        print(f"data: {data}")

        result = self.employee_dao.update(data['employee_id', data])

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def delete(self):
        """Delete a record from the database"""

        print("\nDeleting a employee ...")

        # Grab the employee_id from the stringvar
        id = self.employee_id.get()
        print(f"id: {id}")

        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        employee_dao = EmployeeDAO()
        result = employee_dao.delete(id)

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    

        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def load(self):
        """Retrieve a list of IDs from the database and load them into a listbox"""

        print("\nLoading IDs in list box ...")

        result = self.employee_dao.find_ids(self)
        print(f"result: {result}")

        # Check if there is an entry in the result dictionary
        if "employee_id" in result: 
            list_ids = result['employee_id'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_id.delete(0,tk.END)
            print("Setting doctor_ids in listbox ...")
            for x in list_ids:
                self.lb_id.insert(tk.END, x)
                #print(x)
            pass

    def on_list_select(self, evt):
        """on_list_select() is triggered when a user clicks an item in the listbox"""

        print("\nSelecting an item from the list box ...")

        w = evt.widget

        # index = position of the item clicked in the list, first item is item 0 not 1
        index = int(w.curselection()[0]) 
          
         # value of the item clicked, in our case it's the doctor_id  
        value = w.get(index) 
         
        print(f"index: {index}") 
        print(f"value: {value}")

        # Call find_by_id and populate the stringvars of the form
        employee_dao = EmployeeDAO()
        result = employee_dao.find_by_id(value)

        # { "doctor" : {"doctor_id": "", "firstname": "", etc}}
        print(f"result: {result}") 

        # Grab doctor dict from result dict and use it to populate the fields on the form  
        employee = result['employees']
        self.populate_fields(employee)

    def populate_fields(self, employee):
        """Populate the fields of the form with data"""

        print("\nPopulating fields ...")
        print(f"employee: {employee}")

        # Set the values from the dict to the stringvars
        self.employee_id.set(employee['employee_id'])
        self.last_name.set(employee['last_name'])
        self.first_name.set(employee['first_name'])
        self.phonenumber.set(employee['phonenumber'])
        self.email.set(employee['email'])
        self.address.set(employee['address'])
        self.dob.set(employee['dob'])
        self.hotel_id.set(employee['hotel_id'])

    def validate_fields(self, data):
        """Validate the data entered in the fields of the form"""

        print("\nValidating the data ...")
        print(f"data: {data}")
           
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        # Instantiate an empty list to contain the messages
        message_list = [] 
        
        # Check for blank fields
        # Do not check doc_id as this is generated by the database
        #if len(data['guest_no']==0:
        #    valid_data = False
        #    message_list.append("guest_no is empty")
        if len(data['last_name'])==0:
            valid_data = False
            message_list.append("lastname is empty")
        if len(data['first_name'])==0:
            valid_data = False
            message_list.append("firstname is empty")
        if len(data['phonenumber'])==0:
            valid_data = False
            message_list.append("phonenumber is empty")
        if len(data['email'])==0:
            valid_data = False
            message_list.append("email is empty")
        if len(data['address'])==0:
            valid_data = False
            message_list.append("address is empty")
        if len(data['dob'])==0:
            valid_data = False
            message_list.append("dob is empty")
        if len(data['hotel_id'])==0:
            valid_data = False
            message_list.append("hotel id is empty")
        

        # Other possible checks

        # Implement these as functions in the Validation class so that 
        # other classes can call them
         
        # Check if firstname and lastname contain  
        # only alphabetic characters (and may be certain special characters)
        if not self.validator.is_alphabetic(data['last_name']):
            valid_data = False
            message_list.append("invalid last name")

        if not self.validator.is_alphabetic(data['first_name']):
            valid_data = False
            message_list.append("invalid first name")

        # Check if work_phone follows a certain pattern 
        # i.e. (02) 99999999 or (02) 9999 9999 or +61 3 9999 9999 (international)
        if not self.validator.is_phone_number(data['phonenumber']):
            valid_data = False
            message_list.append("invalid phone number format")
    
        # Check if email follows a certain pattern 
        # i.e contains an @ followed by a dot
        if not self.validator.is_email(data['email']):
            valid_data = False
            message_list.append("invalid email format")

        
                   
        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 value


# ###########
# Main method
# ###########

if __name__ == '__main__':
    """The main method is only executed when the file is 'run' (not imported in another file)"""

    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("XXXXXX System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = EmployeeGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass

