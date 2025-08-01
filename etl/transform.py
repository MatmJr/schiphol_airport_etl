import pandas as pd
import ast

def transform(csv_file, new_csv_file):
    df = pd.read_csv(csv_file)
    df["modeloAviao"] = None
    df['aircraftType'] = df['aircraftType'].apply(ast.literal_eval)

    for i in range(len(df)):
        iata_info = df["aircraftType"][i]
        if 'iataMain' in iata_info:
            valor_a_atribuir = df["aircraftType"][i]['iataMain']
            df.loc[i, "modeloAviao"] = valor_a_atribuir
    
    print(f"Salvo em {new_csv_file}")
    return df.to_csv(new_csv_file)
  
# transform("flights.csv", "transformed_flights.csv")