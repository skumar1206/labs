import requests
homepage = requests.get("http://www.google.com/")

print(homepage.status_code)

raw_script = requests.get("https://raw.githubusercontent.com/skumar1206/labs/main/lab1/lab1.py")
print(raw_script.text)
