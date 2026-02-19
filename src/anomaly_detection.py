import pandas as pd
from data_loader import load_flight_data

def detect_anomalies(df, threshold_hours=2):
    
    # Find all flights delayed more than threshold
    anomalies = df[df['delay_hours'] > threshold_hours].copy()
    normal = df[df['delay_hours'] <= threshold_hours].copy()
    
    # Add a flag column to main dataframe
    df['is_anomaly'] = df['delay_hours'] > threshold_hours
    
    print("=" * 50)
    print("📊 FLIGHT ANOMALY DETECTION REPORT")
    print("=" * 50)
    
    print(f"\n✈️  Total flights analyzed : {len(df)}")
    print(f"✅  On time flights        : {len(normal)}")
    print(f"🚨  Delayed flights (>2hrs): {len(anomalies)}")
    
    on_time_pct = round((len(normal) / len(df)) * 100, 1)
    delay_pct = round((len(anomalies) / len(df)) * 100, 1)
    print(f"\n📈  On-Time Performance    : {on_time_pct}%")
    print(f"📉  Delay Rate             : {delay_pct}%")
    
    print("\n" + "=" * 50)
    print("🚨 ANOMALY FLIGHTS LIST")
    print("=" * 50)
    print(anomalies[['flight_id', 'airline', 
                      'route', 'delay_hours', 
                      'status']].to_string(index=False))
    
    print("\n" + "=" * 50)
    print("📊 DELAYS BY AIRLINE")
    print("=" * 50)
    airline_delays = anomalies.groupby('airline').size()\
                               .reset_index(name='total_delays')\
                               .sort_values('total_delays', ascending=False)
    print(airline_delays.to_string(index=False))
    
    print("\n" + "=" * 50)
    print("📊 DELAYS BY ROUTE")
    print("=" * 50)
    route_delays = anomalies.groupby('route').size()\
                             .reset_index(name='total_delays')\
                             .sort_values('total_delays', ascending=False)
    print(route_delays.to_string(index=False))
    
    # Save anomalies to Excel
    anomalies.to_excel("reports/anomaly_flights.xlsx", index=False)
    print("\n💾 Anomaly report saved to reports/anomaly_flights.xlsx")
    
    return df, anomalies

if __name__ == "__main__":
    df = load_flight_data("data/processed/flight_data_clean.xlsx")
    df, anomalies = detect_anomalies(df)