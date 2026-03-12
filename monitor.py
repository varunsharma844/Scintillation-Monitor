import requests
import datetime
import os

def run_monitor():
    try:
        # 1. Fetch Kp-Index from NOAA
        response = requests.get("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json")
        data = response.json()
        kp = float(data[-1][1])
        
        # 2. Setup IST Time (UTC + 5:30)
        ist_now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
        
        print(f"--- NOIDA SATELLITE MONITOR ---")
        print(f"Time: {ist_now.strftime('%Y-%m-%d %H:%M:%S')} IST")
        print(f"Current Kp Index: {kp}")

        # 3. Threshold Logic
        if kp >= 5.0:
            print("!!! CRITICAL ALERT: G1+ Storm. Signal drops expected on GSAT-30.")
        elif kp >= 4.0:
            print("--- WARNING: Moderate activity. Phase jitter likely.")
        else:
            print("Status: Ionosphere is Stable.")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    run_monitor()
