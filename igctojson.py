import json

def parse_igc_line(line):
    # linie zaczynające się od B zawierają dane GPS
    if not line.startswith('B'):
        return None
    
    # czas
    hh = int(line[1:3])
    mm = int(line[3:5])
    ss = int(line[5:7])
    time_str = f"{hh:02d}:{mm:02d}:{ss:02d}"
    
    # szerokość
    lat_deg = int(line[7:9])
    lat_min = float(line[9:14]) / 1000
    lat_hem = line[14]
    latitude = lat_deg + lat_min / 60
    if lat_hem == 'S':
        latitude = -latitude
    
    # długość
    lon_deg = int(line[15:18])
    lon_min = float(line[18:23]) / 1000
    lon_hem = line[23]
    longitude = lon_deg + lon_min / 60
    if lon_hem == 'W':
        longitude = -longitude
    
    # wysokość GPS (ostatnie 5 znaków)
    altitude = int(line[25:30])  # GPS altitude
    
    return {
        "time": time_str,
        "latitude": round(latitude, 6),
        "longitude": round(longitude, 6),
        "altitude": altitude
    }

# wczytaj plik IGC
positions = []
with open('2024-08-16-XLK-Mar-02.IGC', 'r') as f:
    for line in f:
        line = line.strip()
        data = parse_igc_line(line)
        if data:
            positions.append(data)

# zapisz do JSON
with open('flight.json', 'w') as f:
    json.dump(positions, f, indent=2)

print(f"Zapisano {len(positions)} pozycji do flight.json")

