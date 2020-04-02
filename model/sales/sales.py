""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def data_read():
    data = data_manager.read_table_from_file(DATAFILE, separator=';')
    return data, HEADERS

def get_Id():
    return util.generate_id()

def data_write(data):
    data_manager.write_table_to_file(DATAFILE, data, separator=';')