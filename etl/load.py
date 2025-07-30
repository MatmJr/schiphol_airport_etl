import pandas as pd
from extract import get_endpoint

def save_in_csv(endpoint, csv_name):
    data = get_endpoint(endpoint)
    df = pd.DataFrame([item for page in data for item in page["flights"]])
    df.to_csv(csv_name, index=False)
    print(f"Salvo em {csv_name}")

save_in_csv("flights", "flights.csv")