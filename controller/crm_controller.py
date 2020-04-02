from model.crm import crm
from view import terminal as view
from model import data_manager


def list_customers():
    table = crm.get_table()
    view.print_table(table)

    
def add_customer():
    index_customer_name = 1
    index_Id = 0
    table = crm.get_table()
    Id = list(crm.get_Id())
    name = view.get_input("Customer name: ")
    email = view.get_input("Customer email:")
    subscribtion = view.get_input("Is subscribed to the newsletter? 1: yes, 0: no:")
    table.insert(0, Id)
    view.print_table(table)
    data_manager.write_table_to_file("model/crm/crm.csv", table, separator= ';')
    return table


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    index_email = 2
    email_list = []
    index_name = 1
    table = crm.get_table()
    for c, emails in enumerate(table):
        if '@' in emails[index_email]:
            email_list.append([c, emails[index_email], emails[index_name]] )
    view.print_table(email_list)
    return email_list


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)