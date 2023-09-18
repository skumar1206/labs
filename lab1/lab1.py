import requests
homepage = requests.get("http://www.google.com/")

print(homepage.status_code)
