import urllib.request,json

source = urllib.request.urlopen('http://localhost:8000/user/1').read()
list_of_data= json.loads(source)
print(list_of_data['username'])
print(type(list_of_data))