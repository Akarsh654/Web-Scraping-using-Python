import requests
from bs4 import BeautifulSoup
import texttable as tt

# request then parse the contents of the website
response = requests.get("https://www.covid19kenya.org/")
soup = BeautifulSoup(response.text, "html.parser")  # pass the html object and the type of parser as arguments

# soup.find_all will scrape every element in the table
county_name = iter(soup.select('th a[href]'))
other_data = iter(soup.find_all('td'))
data = []

# This loop will keep repeating till there is data available in the iterator
while True:
    try:
        county = next(county_name).text
        confirmed = next(other_data).text
        recovered = next(other_data).text
        deceased = next(other_data).text
        preview = next(other_data).text

        data.append([county, confirmed, recovered, deceased, preview])

    # Exception will occur when there are no more elements left to iterate through
    except StopIteration:
        break

# Print the table
table = tt.Texttable()  # create texttable object
table.add_rows([(None, None, None, None, None)] + data)  # add an empty row at the beginning for the headers
table.set_cols_align(('c', 'c', 'c', 'c', 'c'))  # 'c' denotes center align
table.header((' County ', ' Confirmed Cases ', ' Recovered ', ' Deceased ', ' Preview '))  # add the headers
print(table.draw())
