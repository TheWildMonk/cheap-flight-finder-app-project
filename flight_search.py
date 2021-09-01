# Import necessary libraries
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Volumes/Workstation/Learning Center/Data Science/"
                        "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")
KIWI_API_KEY = os.getenv("KIWI_API_KEY")


class FlightSearch:
    def __init__(self, city: str):
        self.ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.city = city
        self.iataCode = "TESTING"
