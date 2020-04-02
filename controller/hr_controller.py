from model.hr import hr
from view import terminal as view


def list_employees():
    data_headers = list(hr.data_read())
    data = data_headers[0]
    headers = data_headers[1]
    view.print_table(data,headers)


def add_employee():
    data = list(hr.data_read())
    data = data[0]
    ID = hr.get_ID()
    name = input("Enter name:\n")
    date_of_birth = input("Enter date of birth:\n")
    department = input("Enter department:\n")
    clearance = input("Enter level of clearance:\n")
    adding = [ID, name, date_of_birth, department, clearance]
    data.append(adding)
    hr.data_write(data)


def update_employee(): #does not work and makes no sense
    view.print_error_message("Not implemented yet.")
    '''
    data = list(hr.data_read())
    data = data[0]
    print(data)
    ids = []
    for elem in data:
        for i in range(len(elem)):
            ident = elem[i][0]
            ids.append(ident)
    print(ids)
    ID = view.get_input('Enter ID:\n')
    if ID in ids:
        index = data.index(ID)
        name = view.get_input("Enter name:\n")
        date_of_birth = view.get_input("Enter date of birth:\n")
        department = view.get_input("Enter department:\n")
        clearance = view.get_input("Enter level of clearance:\n")
        adding = [ID, name, date_of_birth, department, clearance]
        data[index] = adding
        hr.data_write(data)
        list_employees()
        
    else:
        view.print_message("ID does not exist in the database.")
        return
'''

def delete_employee():
    data_headers = list(hr.data_read())
    data = data_headers[0]
    print(data)
    to_del = int(input("Select employee to delete:\n"))
    del data[to_del-1]
    hr.data_write(data)


def get_oldest_and_youngest():
    data_headers = list(hr.data_read())
    data = data_headers[0]
    headers = data_headers[1]
    print(len(data))
    j = 0
    birthdays = []
    for i in data:
        elements = data[0+j]
        dates = elements[2]
        date = dates.split("-")
        birthdays.append(date)
        j+=1
    a = 0
    years = []
    for day in birthdays:
        elem = birthdays[0+a]
        year = elem[0]
        years.append(int(year))
        a+=1
    oldest = min(years)
    youngest = max(years)
    index = years.index(oldest)
    index_young = years.index(youngest)
    print("The oldest employee is:")
    view.print_table([data[index]],headers)
    print("")
    print("The youngest employee is:")
    view.print_table([data[index_young]], headers)
def get_average_age():
    data_headers = list(hr.data_read())
    data = data_headers[0]
    headers = data_headers[1]
    j = 0
    birthdays = []
    for i in data:
        elements = data[0+j]
        dates = elements[2]
        date = dates.split("-")
        birthdays.append(date)
        j+=1
    a = 0
    years = []
    for day in birthdays:
        elem = birthdays[0+a]
        year = elem[0]
        years.append(int(year))
        a+=1
    ages = []
    for elem in years:
        age = 2020 - elem
        ages.append(age)
    average = sum(ages)/len(ages)
    print("The average age of employees is:")
    print(average)


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
