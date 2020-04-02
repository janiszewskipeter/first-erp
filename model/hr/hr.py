""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
#data = data_manager.read_table_from_file("model/hr/hr.csv", separator=';')

def data_read():
    data = data_manager.read_table_from_file(DATAFILE, separator=';')
    return data, HEADERS

def get_ID():
    return util.generate_id()

def data_write(data):
    data_manager.write_table_to_file(DATAFILE, data, separator=';')
