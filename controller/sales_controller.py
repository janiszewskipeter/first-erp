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
    Ids = [i[0] for i in data]
    print(Ids)
    Id = view.get_input('Enter Id:\n')
    if Id not in Ids:
        view.print_message("No such Id.")
        return
    index = data.index(Id)
    customer = view.get_input('Enter Customer:\n')
    product = view.get_input('Enter Product:\n')
    price = view.get_input('Enter Price:\n')
    date = view.get_input('Enter Date:\n')
    item_to_add = [Id, customer, product, price, date]
    data[index] = item_to_add
    sales.data_write(data)


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    data = list(sales.data_read())
    data = data[0]
    headers = data[1]
    print(headers)
    prices = [i[3] for i in data]
    max_price = max(prices)
    index = prices.index(max_price)
    data = data[index]
    view.print_table(data, headers)

def get_biggest_revenue_product():
    data = list(sales.data_read())
    data = data[0]
    headers = data[1]
    products= [i[2] for i in data]
    prices = [i[3] for i in data]
    revenues = [products.count(i) for i in products]
    jajko = zip(products, revenues)
    jajko2 = tuple(jajko)
    print(jajko2)
    # for product in products:
    #     revenue = products.count(product) * prices[products.index(product)]

    # index = max(revenues)
    # print(index)
    # result = products[index]
    # view.print_message(result)


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


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