# Import necessary libraries
from data_manager import DataManager
from flight_search import FlightSearch

# Sheety object definition
sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.sheety_get_response()

for each_city in sheet_data["prices"]:
    if each_city["iataCode"] == "":
        # Flight search object definition
        flight_search_manager = FlightSearch(city=each_city["city"])
        location_data = flight_search_manager.kiwi_get_location()
        each_city["iataCode"] = location_data["locations"][0]["code"]
        sheet_data_manager.sheety_put_request(each_city["city"], each_city["iataCode"],
                                              each_city["lowestPrice"], each_city["id"])
    else:
        continue
