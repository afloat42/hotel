# guest_dao_test.py
# Sohil Pachbhaiya
# 5/2/2023

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox

# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option

# From file xxx.py import class Xxxx
from guest_gui import GuestGUI
from employee_gui import EmployeeGUI

# ################
# Global Constants 
# ################


# ####################
# MainGUI Class
# ####################

class MainGUI():

    def __init__(self):   

        print("Creating Main GUI ...")

        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("XXXX System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Guest menu
        # do not use self.create_guest_gui()
        # Will be executed automatically!
        guestmenu = tk.Menu(menubar, tearoff=0)
        guestmenu.add_command(label="Guest", command=self.create_guest_gui)
        menubar.add_cascade(label="Guest", menu=guestmenu)

        # Employee menu
        employeemenu = tk.Menu(menubar, tearoff=0)
        employeemenu.add_command(label="Employee", command=self.create_employee_gui)
        menubar.add_cascade(label="Employee", menu=employeemenu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
    
    
 
    """
    # Beware: There is a built-in function called exit() 
    # with no argument
    def exit(self):
        answer = messagebox.askyesno('Procurement System', 
                    'Are you sure you want to exit?', icon="warning")
        if answer:
            self.root.destroy()
            exit()    
    """        
            
    # Functions to create child frames 
    # when menu options are selected

    def create_guest_gui(self):

        print("\nCreating person GUI ...")

        # Destroy whatever the current GUI is 
        # and create the person GUI
        if self.current_gui:
            self.current_gui.destroy()

        guest_gui = GuestGUI()
        self.current_gui = guest_gui.create_gui(self.root)
        pass

    
    def create_employee_gui(self):

        print("\nCreating employee GUI ...")

        # Destroy whatever the current GUI is 
        # and create the doctor GUI
        if self.current_gui:
            self.current_gui.destroy()

        employee_gui = EmployeeGUI()
        self.current_gui = employee_gui.create_gui(self.root)
        pass




# ###########
# Main method
# ###########

if __name__ == '__main__':

    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = MainGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
