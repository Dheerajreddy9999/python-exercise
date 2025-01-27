import openpyxl

inv_file = openpyxl.load_workbook("/workspaces/python-exercise/exercise/inventory/inventory.xlsx")
product_list = inv_file["Sheet1"]

products_per_supplier = {}

for product_row in range(2, product_list.max_row):