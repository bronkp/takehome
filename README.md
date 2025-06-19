


## Installation

1. Clone the repository
2. Install requirements
```bash
pip install -r requirements.txt
```




    
## Usage/Examples
1. Apply migrations
```
python manage.py migrate
```
2. Make user
```
python manage.py createsuperuser 
```
3. Generate token and save token
```
python manage.py drf_create_token <username>
```
4. Add device either by /admin page or post request, example:
```
curl -X POST http://127.0.0.1:8000/api/device/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
-d '{
  "devEUI": "abcdabcdabcdabcd"
}'
```
5. Make a post request to simulate payload, example:
```
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
6. Check all device and payload entries with a GET request
- Device: 127.0.0.1:8000/api/device/ 
- Payload: 127.0.0.1:8000/api/payload/
