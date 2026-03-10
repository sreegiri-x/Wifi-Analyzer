def check_security(network):

    enc = network["encryption"]

    if not enc:
        return "OPEN NETWORK (UNSAFE)"

    if 1 in enc:
        return "WEP (VERY WEAK)"

    if 2 in enc:
        return "WPA (WEAK)"

    if 3 in enc or 4 in enc:
        return "WPA2/WPA3 (SECURE)"

    return "UNKNOWN"