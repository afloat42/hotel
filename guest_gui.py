# guest_dao_test.py
# Sohil Pachbhaiya
# 5/2/2023

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox

# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option

# From file xxx.py import class Xxxx
from validation import Validation
from guest_dao import GuestDAO


# ################
# Global Constants 
# ################


# ####################
# GuestGUI Class
# ####################
class GuestGUI():
    """GUI class to perform CRUD operations on the doctor table in the database"""

    def __init__(self):   
        """Initialiser"""
    
        # Instantiate a data access object 
        # Contains methods to access the database
        self.guest_dao = GuestDAO()

        # Instantiate a calidation object
        # contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.guest_no = tk.StringVar()
        self.last_name = tk.StringVar()
        self.first_name = tk.StringVar()
        self.phonenumber = tk.StringVar()
        self.dob = tk.StringVar()
        self.email = tk.StringVar()
        self.address = tk.StringVar()
        self.postcode = tk.StringVar()
        self.city = tk.StringVar()
        self.country = tk.StringVar()
        self.passportno = tk.StringVar()
        self.creditcard_no = tk.StringVar()
        self.card_expiry = tk.StringVar()
        self.card_name = tk.StringVar()

        # List of doctor ids - lb for listbox
        self.lb_nos = None

        # Messagebox title
        self.mb_title_bar = "Doctor CRUD"

        pass 

    def create_gui(self, root):
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
        print("\nCreating guest GUI ...")

        # guest_frame = tk.Frame(root).pack() 
        # cannot write the above as pack() does not return anything
        # and need the variable name to refer to it elsewhere
        # DO NOT SPECIFY ANY WIDTH AND HEIGHT OF THE FRAMES 
        # HERE FOR FLEXIBILITY REASONS
        # The height and width or the root window can be specified 
        # in the main GUI (or in the main() method)
        guest_frame = tk.Frame(root)
        guest_frame.pack()

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
        form_frame = tk.Frame(guest_frame)
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
            font=('arial', 10), 
            text = "Guest").grid(row=0, column=0, columnspan=3)

        # row 1: guest_no label, guest_no entry and list_of_nos label
        tk.Label(
            form_frame, 
            text= "Guest Number", 
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
            textvariable=self.guest_no, 
            width=30, 
            bd=1, 
            state=tk.DISABLED).grid(row=1, column=1)
        # guest_no is disabled to prevent user from entering a value
        # guest_no is generated by the database because AUTOINCREMENT 
        # was specified in the database schema
        tk.Label(
            form_frame, 
            text= "Guest Nos", 
            font=('arial', 10)).grid(row=1, column=2)
        
        # row 2: last_name label, last_name entry and listbox of numbers
        tk.Label(
            form_frame, 
            text= "Last name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=2, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.last_name, 
            width=30, 
            bd=1).grid(row=2, column=1)
        # Use the height= option to specify the height, default is 10
        # Use the width= option to specify the number of characters, default is 20
        self.lb_nos = tk.Listbox(form_frame)
        self.lb_nos.grid(row=2, column=2, rowspan=5) 
        # 'self' means instance attribute rather than local variable
        # since python allows using variables before they are declared
        # it does not matter whether lb_ids has been declared or not at the 
        # top of the file before the methods definition
        # Set the method to be called when an item is clicked on the listbox 
        self.lb_nos.bind('<<ListboxSelect>>', self.on_list_select)

        # row 3: first_name label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "First name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=3, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.first_name, 
            width=30, 
            bd=1).grid(row=3, column=1)
        
        # row 4: phone number label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Phone number", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=4, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.phonenumber, 
            width=30, 
            bd=1).grid(row=4, column=1)
        
        # row 5: dob label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Date of Birth", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=5, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.dob, 
            width=30, 
            bd=1).grid(row=5, column=1)

        # row 6: email label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Email", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=6, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.email, 
            width=30, 
            bd=1).grid(row=6, column=1)

        # row 7: address label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Address", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=7, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.address, 
            width=30, 
            bd=1).grid(row=7, column=1)
        
        # row 8: post code label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Postcode", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=8, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.postcode, 
            width=30, 
            bd=1).grid(row=8, column=1)
        
        # row 9: city label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "City", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=9, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.city, 
            width=30, 
            bd=1).grid(row=9, column=1)
        
        # row 10: country label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Country", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=10, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.country, 
            width=30, 
            bd=1).grid(row=10, column=1)
        
        # row 11: passport number label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Passport Number", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=11, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.passportno, 
            width=30, 
            bd=1).grid(row=11, column=1)
        # row 12: credit number label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Credit Number", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=12, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.creditcard_no, 
            width=30, 
            bd=1).grid(row=12, column=1)
        # row 13: card expiry label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "card_expiry", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=13, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.card_expiry, 
            width=30, 
            bd=1).grid(row=13, column=1)
        # row 14: card name label and combobox (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Card Name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=14, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.card_name, 
            width=30, 
            bd=1).grid(row=14, column=1)

        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid with row 
        # and col locations
        # pady to leave a space from frame on top
        button_frame = tk.Frame(guest_frame, pady=10) 
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
        return guest_frame
    
    def clear_fields(self):
        """Clear the fields of the form"""

        print("\nClearing fields ...")

        # Just blank all the fields
        self.guest_no.set("")
        self.last_name.set("")
        self.first_name.set("")
        self.phonenumber.set("")
        self.dob.set("")
        self.email.set("")
        self.address.set("")
        self.postcode.set("")
        self.city.set("")
        self.country.set("")
        self.passportno.set("")
        self.creditcard_no.set("")
        self.card_expiry.set("")
        self.card_name.set("")

    def save(self):
        """Save the data displayed on the form to the database."""


        print("\nSaving a guest ...")

        # Get the data
        data = self.get_fields()   

        if (len(data['guest_no'])==0):
            print("Calling create() as guest_no is absent")
            self.create(data)
        else:
            print("Calling update() as guest_no is present")
            self.update(data) 

    def get_fields(self):
        """Get the data entered in the fields of the form"""

        print("\nGetting fields ...")

        guest = {}
        # guest_no is ignored when creating a record
        guest['guest_no'] = self.guest_no.get() 
        guest['last_name'] = self.last_name.get()
        guest['first_name'] = self.first_name.get()
        guest['phonenumber'] = self.phonenumber.get()
        guest['dob'] = self.dob.get()
        guest['email'] = self.email.get()
        guest['address'] = self.address.get()
        guest['postcode'] = self.postcode.get()
        guest['city'] = self.city.get()
        guest['country'] = self.country.get()
        guest['passportno'] = self.passportno.get()
        guest['creditcard_no'] = self.creditcard_no.get()
        guest['card_expiry'] = self.card_expiry.get()
        guest['card_name'] = self.card_name.get()

        print(f"guest: {guest}")
 
        return guest   
    
    def create(self, data):
        """
        Create a new record in the database.
        A messagebox is used display the outcome (success or failure) 
        of the create operation to the user.

        Parameters (apart from self):
            data: dictionary object containing doctor data to be saved
 
        Return: None
        """

        print("\nCreating a doctor ...")
        print(f"data: {data}")

        result = self.guest_dao.create(data)
        messagebox.showinfo(self.mb_title_bar, result)

        pass

    def update(self, data):
        """Update a record in the database"""

        print("\nUpdating a doctor ...")
        print(f"data: {data}")

        result = self.guest_dao.update(data['guest_no'], data)

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        pass
    
    def delete(self):
        """Delete a record from the database"""

        print("\nDeleting  a doctor ...")
        
        # Grab the doctor_id from the stringvar
        id = self.guest_no.get() 
        print(f"id: {id}")
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        result = self.guest_dao.delete(id)   

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)
        pass
    
    def load(self):
        """Retrieve a list of IDs from the database and load them into a listbox"""

        print("\nLoading IDs in list box ...")

        result = self.guest_dao.find_no()
        print(f"result: {result}")

        # Check if there is an entry in the result dictionary
        if "guest_no" in result: 
            list_ids = result['guest_no'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_nos.delete(0,tk.END)
            print("Setting doctor_ids in listbox ...")
            for x in list_ids:
                self.lb_nos.insert(tk.END, x)
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
        result = self.guest_dao.find_by_nos(value)

        # { "doctor" : {"doctor_id": "", "firstname": "", etc}}
        print(f"result: {result}") 

        # Grab doctor dict from result dict and use it to populate the fields on the form  
        guest = result['guest']
        self.populate_fields(guest)

    def populate_fields(self, guest):
        """Populate the fields of the form with data"""

        print("\nPopulating fields ...")
        print(f"guest: {guest}")

        # Set the values from the dict to the stringvars
        self.guest_no.set(guest['guest_no'])
        self.last_name.set(guest['last_name'])
        self.first_name.set(guest['first_name'])
        self.phonenumber.set(guest['phonenumber'])
        self.dob.set(guest['dob'])
        self.email.set(guest['email'])
        self.address.set(guest['address'])
        self.postcode.set(guest['postcode'])
        self.city.set(guest['city'])
        self.country.set(guest['country'])
        self.passportno.set(guest['passportno'])
        self.creditcard_no.set(guest['creditcard_no'])
        self.card_expiry.set(guest['card_expiry'])
        self.card_name.set(guest['card_name'])

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
        #if len(data['doc_id']==0:
        #    valid_data = False
        #    message_list.append("doc_id is empty")
        if len(data['last_name'])==0:
            valid_data = False
            message_list.append("last name is empty")
        if len(data['first_name'])==0:
            valid_data = False
            message_list.append("first name is empty")
        if len(data['phonenumber'])==0:
            valid_data = False
            message_list.append("phone number is empty")
        if len(data['dob'])==0:
            valid_data = False
            message_list.append("dob is empty")
        if len(data['email'])==0:
            valid_data = False
            message_list.append("email is empty")
        if len(data['address'])==0:
            valid_data = False
            message_list.append("address is empty")
        if len(data['dob'])==0:
            valid_data = False
            message_list.append("dob is empty")
        if len(data['postcode'])==0:
            valid_data = False
            message_list.append("postcode is empty")
        if len(data['city'])==0:
            valid_data = False
            message_list.append("city is empty")
        if len(data['country'])==0:
            valid_data = False
            message_list.append("country is empty")
        if len(data['city'])==0:
            valid_data = False
            message_list.append("city is empty")
        if len(data['passportno'])==0:
            valid_data = False
            message_list.append("passportno is empty")
        if len(data['creditcard_no'])==0:
            valid_data = False
            message_list.append("creditcard_no is empty")
        if len(data['card_expiry'])==0:
            valid_data = False
            message_list.append("card_expiry is empty")
        if len(data['card_name'])==0:
            valid_data = False
            message_list.append("card_name is empty")

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

        return valid_data, message # return 2 values


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
    height = 650
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = GuestGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass



        