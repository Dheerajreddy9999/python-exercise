import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["sheet1"]

products_per_supplier = {}