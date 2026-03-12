import requests
import datetime

def check_noaa():
    try:
        # Fetching latest Kp-Index from NOAA
        response = requests.get("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json")
        data = response.json()
        latest = data[-1]
        return float(latest[1])
    except:
        return 0

def run_monitor():
    kp = check_noaa()
    # Convert to IST (UTC + 5:30)
    ist_now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    print(f"--- NOIDA SATELLITE MONITOR ---")
    print(f"Time: {ist_now.strftime('%Y-%m-%d %H:%M:%S')} IST")
    print(f"Current Kp Index: {kp}")

    if kp >= 5:
        print("!!! CRITICAL: G1+ Storm. Major risk for GSAT-30 / Intelsat links.")
    elif kp >= 4:
        print("--- WARNING: Moderate activity. Expect phase jitter.")
    else:
        print("Status: Ionosphere is Stable.")

if __name__ == "__main__":
    run_monitor()
