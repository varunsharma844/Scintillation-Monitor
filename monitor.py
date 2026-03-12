import requests
import datetime
import os

def run_monitor():
    try:
        response = requests.get("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json")
        data = response.json()
        kp = float(data[-1][1])
        ist_now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
        
        # This makes the output much easier to find in the logs
        print("\n" + "="*45)
        print(f" NOIDA SATELLITE STATUS: {ist_now.strftime('%d %b %Y | %H:%M')} IST")
        print("="*45)
        print(f" CURRENT PLANETARY Kp INDEX: {kp}")
        
        if kp >= 5.0:
            print(" >>> CRITICAL: G1+ Storm. Check GSAT-30/Intelsat links now.")
        elif kp >= 4.0:
            print(" >>> WARNING: High activity. Expect downlink jitter.")
        else:
            print(" >>> STATUS: All signals stable. No action needed.")
        print("="*45 + "\n")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    run_monitor()
