from scanner import scan_wifi
from security_check import check_security
from rich.console import Console
from rich.table import Table

console = Console()


    
def signal_quality(signal):

    if signal >= -50:
        return "Excellent"
    elif signal >= -60:
        return "Good"
    elif signal >= -70:
        return "Fair"
    else:
        return "Weak"

def detect_channel_usage(networks):

    channels = {}

    for n in networks:
        ch = n["channel"]

        if ch not in channels:
            channels[ch] = 0

        channels[ch] += 1

    return channels
def detect_rogue_access_points(networks):

    ssid_map = {}

    for n in networks:

        ssid = n["ssid"]
        bssid = n["bssid"]

        if ssid not in ssid_map:
            ssid_map[ssid] = set()

        ssid_map[ssid].add(bssid)

    rogue = []

    for ssid, bssids in ssid_map.items():
        if len(bssids) > 1:
            rogue.append(ssid)

    return rogue
    
def main():

    networks = scan_wifi()

    table = Table(title="WiFi Network Analyzer")

    table.add_column("SSID", style="cyan")
    table.add_column("Signal (dBm)", justify="center")
    table.add_column("Quality", justify="center")
    table.add_column("Security", justify="center")

    for n in networks:

        signal = str(n["signal"])
        quality = signal_quality(n["signal"])
        security = check_security(n)

        table.add_row(
            n["ssid"],
            signal,
            quality,
            security
        )

    console.print(table)


if __name__ == "__main__":
    main()
    