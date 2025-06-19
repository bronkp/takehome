


## Installation

1. Clone the repository
2. Install requirements
```bash
pip install -r requirements.txt
```




    
## Usage/Examples
1. Apply migrations
```bash
python manage.py migrate
```
2. Make user
```bash
python manage.py createsuperuser 
```
3. Generate token and save token
```bash
python manage.py drf_create_token <username>
```
4. Add device either by /admin page or POST request, example:
```bash
curl -X POST http://127.0.0.1:8000/api/device/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
-d '{
  "devEUI": "abcdabcdabcdabcd"
}'
```
5. Make a POST request to simulate payload, example:
```bash
curl -X POST http://127.0.0.1:8000/api/payload/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
-d '{
  "fCnt": 100,
  "devEUI": "abcdabcdabcdabcd",
  "data": "AQ==",
  "rxInfo": [
    {
      "gatewayID": "1234123412341234",
      "name": "G1",
      "time": "2022-07-19T11:00:00",
      "rssi": -57,
      "loRaSNR": 10
    }
  ],
  "txInfo": {
    "frequency": 86810000,
    "dr": 5
  }
}'

```
6. Check all device and payload entries with a GET request (token still required)
- All Devices: 127.0.0.1:8000/api/device/
- One Device: 127.0.0.1:8000/api/device/{devEUI}
- All Payloads: 127.0.0.1:8000/api/payload/
## Considerations
If this were a real project SECRET_KEY and DEBUG should set with environmental variables.
Currently, DEBUG is hardcoded True.
