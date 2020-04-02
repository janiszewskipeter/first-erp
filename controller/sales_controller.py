from model.sales import sales
from view import terminal as view


def list_transactions():
    data_headers = list(sales.data_read())
    data = data_headers[0]
    headers = data_headers[1]
    view.print_table(data, headers)

def add_transaction():
    data = list(sales.data_read())
    data = data[0]
    Id = sales.get_Id()
    customer = view.get_input('Enter Customer:\n')
    product = view.get_input('Enter Product:\n')
    price = view.get_input('Enter Price:\n')
    date = view.get_input('Enter Date:\n')
    item_to_add = [Id, customer, product, price, date]
    data.append(item_to_add)
    sales.data_write(data)

def update_transaction():
    data = list(sales.data_read())
    data = data[0]
    ids = [i[0] for i in data]
    Id = view.get_input('Enter Id:\n')
    # if Id not in Ids:
    #     view.print_message("No such Id.")
    #     return
    index = ids.index(Id)
    customer = view.get_input('Enter Customer:\n')
    product = view.get_input('Enter Product:\n')
    price = view.get_input('Enter Price:\n')
    date = view.get_input('Enter Date:\n')
    item_to_add = [Id, customer, product, price, date]
    data[index] = item_to_add
    sales.data_write(data)
    return
    
def delete_transaction():
    data = list(sales.data_read())
    print(data)
    data = data[0] 
    headers = data[1]
    id_to_delete = view.get_input('Enter Id to delete:\n')
    ids = [i[0] for i in data]
    index = ids.index(id_to_delete)
    del data[index]
    print(data)
    sales.data_write(data)
    

def get_biggest_revenue_transaction():
    data = list(sales.data_read())
    print(data)
    data = data[0]
    headers = data[1]
    prices = [float(i[3]) for i in data]
    max_price = max(prices)
    index = prices.index(max_price)
    data = data[index]
    print(headers)
    print(data)
    view.print_table(data, headers)

def get_biggest_revenue_product():
    data = list(sales.data_read())
    data = data[0]
    headers = data[1]
    revenues = []
    products= [i[2] for i in data]
    prices = [float(i[3]) for i in data]
    quantity = [int(products.count(i)) for i in products]
    revenues = [i * quantity[prices.index(i)] for i in prices]
    max_rerevenue_index = revenues.index(max(revenues))
    result = products[max_rerevenue_index]
    view.print_message(result)
    
    
def count_transactions_between():
    start_date = view.get_input('Enter start date')
    end_date = view.get_input('Enter end date')
    data = list(sales.data_read())
    data = data[0]
    dates = [start_date,end_date]
    table_dates = [i[4] for i in data]
    print(table_dates)
    result = (table_dates.index(dates[1]) - table_dates.index(dates[0])) + 1
    view.print_message(result)

def sum_transactions_between():
    start_date = view.get_input('Enter start date')
    end_date = view.get_input('Enter end date')
    data = list(sales.data_read())
    data = data[0]
    dates = [start_date,end_date]
    table_dates = [i[4] for i in data]
    start_index = table_dates.index(dates[0])
    end_index = table_dates.index(dates[1])
    prices = [float(i[3]) for i in data]
    data_range = prices[start_index:end_index]
    result = sum(data_range )
    view.print_message(result)

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)