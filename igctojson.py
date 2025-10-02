import json

def parse_igc_line(line):
    if not line.startswith('B'):
        return None
    
    # czas
    hh = int(line[1:3])
    mm = int(line[3:5])
    ss = int(line[5:7])
    time_str = f"{hh:02d}:{mm:02d}:{ss:02d}"
    
    # szerokość (DDMMmmmN/S)
    lat_deg = int(line[7:9])
    lat_min = float(line[9:14]) / 1000
    lat_hem = line[14]
    latitude = lat_deg + lat_min / 60
    if lat_hem == 'S':
        latitude = -latitude
    
    # długość (DDDMMmmmE/W)
    lon_deg = int(line[15:18])
    lon_min = float(line[18:23]) / 1000
    lon_hem = line[23]
    longitude = lon_deg + lon_min / 60
    if lon_hem == 'W':
        longitude = -longitude
    
    # wysokość GPS (ostatnie 5 znaków z E/W pola)
    try:
        altitude = int(line[25:30])
    except ValueError:
        altitude = None
    
    return {
        "time": time_str,
        "latitude": round(latitude, 6),
        "longitude": round(longitude, 6),
        "altitude": altitude
    }

def parse_igc_file(input_file):
    positions = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            data = parse_igc_line(line)
            if data:
                positions.append(data)
    return positions

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python parse_igc.py input.IGC output.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    positions = parse_igc_file(input_file)

    with open(output_file, 'w') as f:
        json.dump(positions, f, indent=2)
    
    print(f"Zapisano {len(positions)} pozycji do {output_file}")

