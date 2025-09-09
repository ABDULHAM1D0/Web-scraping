import pandas as pd
from googlesearch import search
import re
from bs4 import BeautifulSoup
import time
import openpyxl
import json


# company_names = ['AMAZON', 'MICROSOFT', 'TESLA', 'APPLE', 'LINUX', 'LAZIKA']
# One way
def searching_url(com_name):
    query = f"{com_name} OFFICIAL WEBSITE"
    attempt = 0
    while attempt < 3:
        try:
            searching = search(query, num_results=5, timeout=50)
            for link in searching:
                if "facebook" not in link and 'linkedin' not in link:
                    return link
                print(link)
            return None
        except Exception as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}. Retrying...")
            time.sleep(2 ** attempt)
    return None
# Second way
def find_official_website(company_name, serpapi_api_key):
    params = {
        "engine": "google",
        "q": company_name,
        "api_key": serpapi_api_key,
        "num": 5
    }

# with open("company_names.csv", "r") as file:
#     company_names = file.readlines()
#
# cleaned_data = []
# for company_name in company_names:
#     # company_name = re.sub('[^a-zA-Z]', ' ', company_name)
#     company_name = re.sub(r'[^a-zA-Z0-9., ]', '', company_name)
#     company_name = re.sub(r'\s+', ' ', company_name).strip()
#     print(company_name)
#     cleaned_data.append(company_name)
# print(cleaned_data)

wb = openpyxl.load_workbook("WORLDFEST SPONSOR.xlsx")

# Select the active sheet
sheet = wb.active

# Read and print the data
dataset_from_excel = []
for row in sheet.iter_rows(min_row=1, values_only=True):
    str_type = str(row[0])
    # print(str_type)
    dataset_from_excel.append(str_type)

cleaned_data = []
for data in dataset_from_excel[1:-1]:
    data = re.sub(r'\s+', ' ', data).strip()
    cleaned_data.append(data)


dictionary_urls = {}
for company_name in cleaned_data:
    dictionary_urls[company_name] = searching_url(company_name)
print(dictionary_urls)

# try:
#     dt = pd.DataFrame(dictionary_urls, columns=['name', 'url'])
#     print(dt)
# except Exception as e:
#     print(e)
#     dt = pd.DataFrame(dictionary_urls)
# finally:
#     dt.to_csv('final_data.txt', index=False)
#




