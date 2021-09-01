# Import necessary libraries
import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Volumes/Workstation/Learning Center/Data Science/"
                        "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")
SHEETY_API_KEY = os.getenv("SHEETY_API_FLIGHT")


class DataManager:
    """A class to represent all the functionalities
    of the Sheety API."""
    def __init__(self):
        self.ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/prices"

    def sheety_get_response(self, call_sheety: bool = False):
        """Get response function for Sheety API"""
        if call_sheety:
            response = requests.get(url=self.ENDPOINT)
            response.raise_for_status()
            data = response.json()
            return data
        else:
            data = {
                'prices': [
                    {'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 800},
                    {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 866},
                    {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 2183},
                    {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 1500},
                    {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 687},
                    {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 367},
                    {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 693},
                    {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 1394},
                    {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 1708},
                    {'city': 'Kolkata', 'iataCode': '', 'id': 11, 'lowestPrice': 276},
                    {'city': 'Phuket', 'iataCode': '', 'id': 12, 'lowestPrice': 469},
                    {'city': 'Kathmandu', 'iataCode': '', 'id': 13, 'lowestPrice': 1184},
                    {'city': 'Singapore', 'iataCode': '', 'id': 14, 'lowestPrice': 1469}
                ]
            }
            return data
