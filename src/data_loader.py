import pandas as pd

def load_flight_data(filepath):
    # Read flight_id column as text to prevent scientific notation
    df = pd.read_excel(filepath, dtype={'flight_id': str})
    
    # Fix any remaining scientific notation like 6.00E+201
    df['flight_id'] = df['flight_id'].str.replace(r'(\d+\.?\d*)[Ee]\+0*(\d+)', 
                                                lambda m: f"6E-{m.group(2)}", 
                                                regex=True).str.upper()
    
    print("✅ Data loaded successfully!")
    print(f"Total flights: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst 5 rows:")
    print(df[['flight_id', 'airline', 'route', 'status', 'delay_hours']].head())
    return df

if __name__ == "__main__":
    df = load_flight_data("data/processed/flight_data_clean.xlsx")