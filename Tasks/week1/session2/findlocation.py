import requests

url= 'https://api.ipify.org/?format=json'


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    my_ip:str= data.get('ip')
else:
    print(f"faild to get ip{response.status_code}")

print(f"my ip is : {my_ip}")
loc_url= f'https://ipinfo.io/{my_ip}/geo'

print(loc_url)

response2=requests.get(loc_url)

if response2.status_code == 200 :
    data2 = response2.json()
    myloc:str = data2.get("loc")
else:
    print(f"faild to get loc{response2.status_code}")

print(f"my location Coordinates is {myloc}")

