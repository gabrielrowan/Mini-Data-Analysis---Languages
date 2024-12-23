# Foreign Languages Analysis

## Intro

This project web scrapes the table of the most commonly spoken languages from this Wikipedia page using BeautifulSoup: 
https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers

It parses the html and outputs the relevant table data to a `.csv` file. 

This `.csv' file is then imported into Jupyter Notebooks and analysed for insights 

## Technologies used 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

## Files

**To view the data analysis including charts, click on the `Languages_analysis.ipynb` file**

- `get_html.py` - retrieves the html from the wikipedia web page
- `languages_html.txt` - the html output file of `get_html.py`
- `parse_html.py` - parses the html using `BeautifulSoup4`, gets the relevant table data and outputs to a `.csv` file
- `languages_wiki.csv` - the output `.csv` from `parse_html.py`
- `Languages_analysis.ipynb` - the Jupyter Notebook containing the data analysis of the `.csv` file
- `Analyse.py` - a draft of the questions I wanted to answer using this dataset

## Data Analysis extract

Bar chart of the native speakers of all Romance and Germanic languages

![bar chart - romance and germanic languages](https://github.com/user-attachments/assets/e9d83550-a91e-4aab-aadc-fc88c5a2b7c7)

## Questions for Data Analysis

Here are the list of questions I answered through analysing the file with python's pandas:

1) What is the total number of native speakers across all languages in the dataset?
2) How many different types of language family are there?
3) What is the total number of native speakers per language family?
4) What are the top 3 most common language families?
5) Create a pie chart showing the top 3 most common language families
6) What is the most commonly occuring Language family - branch pair?
7) Which languages are Sino-Tibetan in the table?
8) Display a bar chart of the native speakers of all Romance and Germanic languages
9) What percentage of total native speakers is represented by the top 5 languages?
10) Which branch has the most native speakers, and which has the least?

Answers can be found in the `languages_analysis.ipynb` file

## Final Words

Project completed December 2024 by Gabriel Rowan :smiley_cat:

    
