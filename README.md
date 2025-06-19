


## Installation

1. Clone the repository
2. Install requirments
```bash
pip install -r requirments.txt
```




    
## Usage/Examples
1. Make user
```
python manage.py createsuperuser 
```
2. Generate token and save token
```
python manage.py drf_create_token <username>
```
3. Add device either by /admin page or post request, example:
```
curl -X POST http://127.0.0.1:8000/api/device/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
  -d '{ 
        "devEUI": "abcdabcdabcdabcd", 
    }' 
```
4. Make a post request to simulate payload, example:
```
curl -X POST http://127.0.0.1:8000/api/payload/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
  -d '{ 
        "fCnt": 100, 
        "devEUI": "abcdabcdabcdabcd", 
        "data": "AQ==", 
            "rxInfo": [ 
                {"gatewayID": "1234123412341234", 
                "name": "G1","time": "2022-07-19T11:00:00", 
                "rssi": -57,"loRaSNR": 10} 
                ], 
        "txInfo": {"frequency": 86810000,"dr": 5} 
    }' 

```
5. Check device and payload entries with a GET request
- Device: 127.0.0.1:8000/api/device/ 
- Payload: 127.0.0.1:8000/api/payload/
