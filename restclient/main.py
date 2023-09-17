import json
import requests
geturl="http://127.0.0.1:8005/getcourses"
posturl="http://127.0.0.1:8005/insertcourse"

coursejson=json.dumps({"author_name":"futurex","course":"new course by SM and NM and ZM","course_section":{"section1":"value189273","section2":"value223675"},"creation_date":"2023-09-11"})
response2=requests.post(posturl,coursejson)
print(response2)
print(response2.text)

response1=requests.get(geturl)
print(response1)
print(response1.text)
