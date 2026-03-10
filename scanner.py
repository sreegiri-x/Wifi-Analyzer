import pywifi
import time

def clean_ssid(ssid):
    return ssid.encode("utf-8", "ignore").decode("utf-8")

def scan_wifi():

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)

    results = iface.scan_results()

    networks = []

    for network in results:

        if network.ssid == "":
            continue

        networks.append({
            "ssid": clean_ssid(network.ssid),
            "signal": network.signal,
            "encryption": network.akm,
            "bssid": network.bssid,
            "channel": network.freq
        })

    return networks