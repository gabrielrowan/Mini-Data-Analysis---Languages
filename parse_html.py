from bs4 import BeautifulSoup
import pandas as pd

with open("languages_html.txt", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

# get table
top_languages_table = soup.select_one('.wikitable.sortable.static-row-numbers')

# get column names
columns = top_languages_table.find_all("th")
column_titles = [column.text.strip() for column in columns]

# get table rows
table_data = top_languages_table.find_all("tr")

# define dataframe
df = pd.DataFrame(columns=column_titles)

# get table data
for row in table_data[1:]:
    row_data = row.find_all('td')
    row_data_txt = [row.text.strip() for row in row_data]
    print(row_data_txt)
    df.loc[len(df)] = row_data_txt 


df.to_csv(r'languages_wiki.csv', index=False, encoding='utf-8-sig')
