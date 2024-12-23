# Foreign Languages Analysis

## Intro

This project web scrapes the table of the most commonly spoken languages from this Wikipedia page: 
https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers

It parses the html and outputs the relevant table data to a `.csv` file. 

This `.csv' file is then imported into Jupyter Notebooks and analysed for insights 

## Files

- `get_html.py` - retrieves the html from the wikipedia web page
- `languages_html.txt` - the html output file of `get_html.py`
- `parse_html.py` - parses the html using `BeautifulSoup4`, gets the relevant table data and outputs to a `.csv` file
- `languages_wiki.csv` - the output `.csv` from `parse_html.py`
- `Lnaguages_analysis.ipynb` - the Jupyter Notebook containing the data analysis of the `.csv` file
- `Analyse.py` - a draft of the questions I wanted to answer using this dataset

## 
