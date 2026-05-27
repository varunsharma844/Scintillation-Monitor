import requests
import datetime
import os

def run_monitor():
    try:
        # Fetching latest Kp-Index from NOAA
        response = requests.get("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json")
        data = response.json()
        
        # FIX: The API now returns a list of dictionaries. 
        # We read the 'kp' key from the last object directly.
        latest_entry = data[-1]
        kp = float(latest_entry.get('kp', latest_entry.get('Kp', 0)))
        
        # Setup IST Time (UTC + 5:30)
        ist_now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
        
        print("\n" + "="*45)
        print(f" NOIDA SATELLITE STATUS: {ist_now.strftime('%d %b %Y | %H:%M')} IST")
        print("="*45)
        print(f" CURRENT PLANETARY Kp INDEX: {kp}")
        
        if kp >= 5.0:
            print(" >>> CRITICAL: G1+ Storm. Signal drops expected on C-band links.")
        elif kp >= 4.0:
            print(" >>> WARNING: High activity. Expect downlink phase jitter.")
        else:
            print(" >>> STATUS: All signals stable. No action needed.")
        print("="*45 + "\n")
            
    except Exception as e:
        print(f"Error parsing data: {e}")

if __name__ == "__main__":
    run_monitor()
