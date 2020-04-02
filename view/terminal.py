from tabulate import tabulate


def print_menu(title, list_options):
    """Prints options in standard menu format like this:
    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program
    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title, '\n')

    for count, option in enumerate(list_options):   # TODO move 0th element to end
        print(count, option)




def print_message(message):
    """Prints a single message to the terminal.
    Args:
        message: str - the message
    """
    
    print(message, '\n')


def print_general_results(result, label):
    
    #if result, label is float:


    formatted_result = "{:.2f}".format(result)
    print(formatted_result)

    formatted_label = "{:.2f}".format(label)
    print(formatted_label)
    
    
    
    # Prints out any type of non-tabular data.
    # It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    # lists/tuples (like "@label: \n  @option1; @option2"), and dictionaries
    # (like "@label \n  @key1: @value1; @key2: @value2")
    
    
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
<<<<<<< HEAD
def print_table(table, headers):
=======
<<<<<<< HEAD
def print_table(table, headers): # Grzesiek
=======
def print_table(table):
>>>>>>> 5d6c10897a4a88fd49d56f27f1ed214e5c99d623
>>>>>>> 5ce35895aa43d2b800249107349092e3f5818ed5
    """Prints tabular data like above.
    Args:
        table: list of lists - the table to print out
    """
<<<<<<< HEAD
    print(tabulate(table, headers,  tablefmt="pretty"))
=======
    print(tabulate(table, headers, tablefmt="pretty"))
>>>>>>> 5ce35895aa43d2b800249107349092e3f5818ed5


def get_input(label):
    """Gets single string input from the user.
    Args:
        label: str - the label before the user prompt
    """
    return input(label)

# def get_inputs(labels):
    labels = ['Enter Customer:\n','Enter Customer:\n','Enter Customer:\n','Enter Customer:\n']
    val1 = imput(labels[0])

    return [val1,val1,val1,val1,]


#     """Gets a list of string inputs from the user.

#     Args:
#         labels: list - the list of the labels to be displayed before each prompt
#     """
#     pass


def print_error_message(message):
    
    """Prints an error message to the terminal.
    Args:
        message: str - the error message
    """

    print(message, '\n')