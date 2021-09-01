# Import necessary libraries
from data_manager import DataManager

sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.sheety_get_response()
print(sheet_data)
