"""
    Graded on:
    Program correctly searches the DuckDuckGo api for the search string
    Program searches the DuckDuckGo api only once
    Program tests that each president is present in the response
"""
#Query API to find names of all the presidents
#Add all names to a list within the program
#Test the list: search the list and compare it to the names in the self-typed list to ensure all presidents are present

import requests

master_president_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Van Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump", "Biden"]

url_ddg = "https://api.duckduckgo.com"

#get the data about the presidents
response = requests.get(url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json")

#read that data into a variable
json_data = response.json()

for key in json_data:
    print(key)
#create a list for storing the name of each president from the API
api_president_last_list = []
for president_last in json_data:
    #if the name in the search matches a name in the master list, append the name to this list
    #if president_last in master_president_list:
    api_president_last_list.append(president_last['url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json"'])

list_without_duplicates = set(api_president_last_list)
#How many items are in the url list (Should be 5000 since we have 5000 photos in our dataset)?
print(len(api_president_last_list))
print(len(list_without_duplicates))


def test_for_presidents():
    r = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    json_data_here = r.json()
    assert "presidents%20of%20the%20united%20states" in json_data_here["RelatedTopics"]


test_for_presidents()
