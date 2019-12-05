# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# MKim, 12.5.2019,Modified to complete assignment 9
# ------------------------------------------------------------------------ #

# Import modules as needed
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class
    from ProcessingClasses import FileProcessor as Fp # FileProcessor class
    from IOClasses import EmployeeIO as Eio # EmployeeIO class
else:
    raise Exception("This file was not created to be imported")
# Data
lstTable = []

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

while True:
    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    choice = Eio.input_menu_options()

    if choice == "1": # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstTable)
    elif choice == "2": # Let user add data to the list of employee objects
        EmpEntered = Eio.input_employee_data()
        lstTable.append(EmpEntered)
    elif choice == "3": # let user save current data to file
        Fp.save_data_to_file("EmployeeData2.txt",lstTable)
    elif choice == "4": # Let user exit program
        break
    else:
        raise Exception("Invalid input. Enter 1-4 only!")

# End of Main Body of Script  ---------------------------------------------------- #