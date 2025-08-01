from etl.extract import get_endpoint
from etl.load import save_in_csv
from etl.transform import transform
import os


os.makedirs("datasets", exist_ok=True)

save_in_csv("flights", "datasets/flights.csv")
transform("datasets/flights.csv", "datasets/transformed_flights.csv")