# IGC to JSON Converter

This Python script parses IGC flight log files (paraglider, glider) and converts the GPS track points into a JSON file containing time, latitude, longitude, and GPS altitude.

## Usage

```bash
python igctojson.py input_file.IGC output_file.json
````

* `input_file.IGC` – path to the IGC file to parse
* `output_file.json` – path where the JSON output will be saved

## Example

```bash
python igctojson.py 2024-08-16-XLK-Mar-02.IGC flight.json
```

The resulting JSON will contain an array of positions:

```json
[
  {
    "time": "14:45:09",
    "latitude": 49.787767,
    "longitude": 19.225133,
    "altitude": 900
  },
  ...
]
```

## Notes

* Only `B`-records in the IGC file are processed.
* Altitudes are taken directly from GPS data.
* Latitude and longitude are converted to decimal degrees.

