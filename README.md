# py-proxy
A simple proxy server written in python3

## Usage
### py-proxy.py
```shell script
python3 py-proxy.py
```
```python
import requests
payload = {}
payload['url'] = 'https://www.baidu.com/'
payload['headers'] = "{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}"
payload['method'] = 'GET'
response = requests.get('http://127.0.0.1:3128/proxy', params=payload, timeout=5)
```

### py-proxy2.py
```shell script
python3 py-proxy2.py
```
```python
import requests
url = 'http://www.baidu.com/'
proxies = {'http': 'http://127.0.0.1:3128'}
response = requests.get(url, proxies=proxies, timeout=5)
```