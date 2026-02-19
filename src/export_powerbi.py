import pandas as pd
from data_loader import load_flight_data
from anomaly_detection import detect_anomalies

def export_for_powerbi():
    
    # Load and process data
    df = load_flight_data("data/processed/flight_data_clean.xlsx")
    df, anomalies = detect_anomalies(df)
    
    # Add extra columns useful for Power BI
    df['date'] = pd.to_datetime(df['scheduled_departure']).dt.date
    df['hour'] = pd.to_datetime(df['scheduled_departure']).dt.hour
    df['day_name'] = pd.to_datetime(df['scheduled_departure']).dt.day_name()
    df['delay_minutes'] = df['delay_hours'] * 60
    df['delay_category'] = pd.cut(
        df['delay_hours'],
        bins=[-1, 0, 0.5, 1, 2, 5],
        labels=['On Time', 'Minor (<30 min)',
                'Moderate (30-60 min)',
                'Significant (1-2 hrs)',
                'Severe (>2 hrs)']
    )

    # Save main flight data
    df.to_excel("data/processed/powerbi_flights.xlsx", index=False)
    print("✅ Main flight data exported!")

    # Save daily summary
    daily = df.groupby('date').agg(
        total_flights=('flight_id', 'count'),
        delayed_flights=('is_anomaly', 'sum'),
        avg_delay=('delay_hours', 'mean'),
        max_delay=('delay_hours', 'max')
    ).reset_index()
    daily['on_time_pct'] = round(
        (1 - daily['delayed_flights'] / daily['total_flights']) * 100, 1
    )
    daily.to_excel("data/processed/powerbi_daily.xlsx", index=False)
    print("✅ Daily summary exported!")

    # Save airline summary
    airline = df.groupby('airline').agg(
        total_flights=('flight_id', 'count'),
        delayed_flights=('is_anomaly', 'sum'),
        avg_delay=('delay_hours', 'mean'),
        max_delay=('delay_hours', 'max')
    ).reset_index()
    airline['on_time_pct'] = round(
        (1 - airline['delayed_flights'] / airline['total_flights']) * 100, 1
    )
    airline.to_excel("data/processed/powerbi_airline.xlsx", index=False)
    print("✅ Airline summary exported!")

    # Save route summary
    route = df.groupby('route').agg(
        total_flights=('flight_id', 'count'),
        delayed_flights=('is_anomaly', 'sum'),
        avg_delay=('delay_hours', 'mean'),
        max_delay=('delay_hours', 'max')
    ).reset_index()
    route['on_time_pct'] = round(
        (1 - route['delayed_flights'] / route['total_flights']) * 100, 1
    )
    route.to_excel("data/processed/powerbi_route.xlsx", index=False)
    print("✅ Route summary exported!")

    print("\n🎉 All files exported to data/processed/")
    print("📂 Files ready for Power BI:")
    print("   - powerbi_flights.xlsx  → main data")
    print("   - powerbi_daily.xlsx    → daily trends")
    print("   - powerbi_airline.xlsx  → airline performance")
    print("   - powerbi_route.xlsx    → route analysis")

if __name__ == "__main__":
    export_for_powerbi()