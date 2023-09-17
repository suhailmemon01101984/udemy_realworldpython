import requests
url="http://127.0.0.1:8005/getcourses"
response=requests.get(url)
print(response)
print(response.text)