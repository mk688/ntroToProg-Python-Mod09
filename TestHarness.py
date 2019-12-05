
# ---------------------------------------------------------- #
# Title: Testing Person, Employee, FileProcessor, and EmployeeIO class
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MKim, 12.7.2019, Modified for Assignment 09
#       to test the Person, Employee, FileProcessor, and EmployeeIO classes
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Person as Per # Person classes
    from DataClasses import Employee as Emp  # Employee class
    from ProcessingClasses import FileProcessor as Fp  # FileProcessor classes
    from IOClasses import EmployeeIO as Eio # EmployeeIO class
else:
    raise Exception("This file was not created to be imported")

# Test the Person class
objP1 = Per("Bob", "Smith")
objP2 = Per("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test the Employee class
objE1 = Emp(1, "Bob", "Smith")
objE2 = Emp(2, "Sue", "Jones")
lstTable = [objE1, objE2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test FileProcessor class
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test EmployeeIO classes
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
Eio.print_menu_items()
print(Eio.input_menu_options())