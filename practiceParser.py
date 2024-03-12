from bs4 import BeautifulSoup
import requests
#Scrapes the webpage
URL = "https://realpython.github.io/fake-jobs/"
page =requests.get(URL)
#parses the html into a soup object
soup = BeautifulSoup(page.content, "html.parser")
#finds the container and creates an iterable array
results = soup.find(id="ResultsContainer")
jobElements = results.find_all("div",class_="card-content")
#iterates through the array for specific attributes
for jobElement in jobElements:
    titleElement = jobElement.find("h2",class_="title") #looks for a h2 header with a class "title" i.e.: h2 class="title*
    companyElement = jobElement.find("h3",class_="company") #looks for a h3 header with a class "company"
    locationElement = jobElement.find("p",class_="location") #looks for a p body with a class "location"
    #.text below just returns the text value for the element and strip() removes white space
    print(titleElement.text.strip())
    print(companyElement.text.strip())
    print(locationElement.text.strip())
    print()