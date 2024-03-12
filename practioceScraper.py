import requests
#scrapes the data raw
URL = "https://realpython.github.io/fake-jobs/"
page =requests.get(URL)
#prints out raw text
print(page.text)