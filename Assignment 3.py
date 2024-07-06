import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO



def main():
    # Step 1: Retrieve the specified webpage as raw HTML using the requests library
    url = "https://en.wikipedia.org/wiki/List_of_Canadian_provinces_and_territories_by_historical_population"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage.")
        return
    html_content = response.content

    # Step 2: Decode the HTML into a tree-structured Python object with the BeautifulSoup library
    soup = BeautifulSoup(html_content, 'html.parser')

    # Step 3: Utilize BeautifulSoup to identify and extract only the tables we're interested in
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Step 4: Merge the tables, sanitize the text, and transform them into a single Python dictionary
    data_dictionary = {}
    for index, table in enumerate(tables):
        dataframe = pd.read_html(StringIO(str(table)))[0]
        if dataframe.columns.nlevels > 1:
            dataframe.columns = dataframe.columns.droplevel(0)  # Tables where the column headers are organized in multiple rows, ie "MultiIndex"
        data_dictionary[f"table_{index}"] = dataframe

    # Step 5: Construct a pandas dataframe out of this dictionary
    combined_df = pd.concat(data_dictionary.values(), ignore_index=True)
    combined_df.to_csv('combined_population_data.csv', index=False)
    print("Combined DataFrame saved as 'combined_population_data.csv'.")

    # Step 6:  Locate all h2 elements on the HTML page and display their text content
    h2_elements = [h2.text.strip() for h2 in soup.find_all('h2')]
    print("H2 Elements:", h2_elements)

    # Step 7: Generate a list of all the hyperlinks embedded within the tables
    links = []
    for table in tables:
        for a in table.find_all('a', href=True):
            links.append(a['href'])

    # Print hyperlinks
    print("All the hyperlinks embedded within the tables:")
    for link in links:
        print(link)

    # Step 8: Download every webpage by traversing the links included in the list created in the previous step.
    base_url = "https://en.wikipedia.org"
    linked_pages_content = {}
    for link in links:
        full_url = base_url + link
        link_response = requests.get(full_url)
        if link_response.status_code == 200:
            linked_pages_content[full_url] = link_response.content
            print(f"Downloaded content: {full_url}")
        else:
            print(f"Failed to download content, Status code: {link_response.status_code}")

if __name__ == "__main__":
    main()





