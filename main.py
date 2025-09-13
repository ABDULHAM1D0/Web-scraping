import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import openpyxl

def scrape_phone_email_turkish(url):
    # Scraping number and email from url
    try:
        url = url.strip()
        if not url.startswith("http"):
            url = "http://" + url  # Add http if missing

        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError if bad status

        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.get_text()

        # Emails regex (same)
        emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text))

        # Turkish phone number regex
        phone_pattern = re.compile(r'''
            (?:\+90\s*|0)?               # Country code +90 or leading 0, optional
            (?:\(?\d{3}\)?[\s\-\.]*)    # Area code with or without parentheses
            \d{3}[\s\-\.]*              # First 3 digits
            \d{2}[\s\-\.]*              # Next 2 digits
            \d{2}                       # Last 2 digits
        ''', re.VERBOSE)

        phones = set(match.group().strip() for match in phone_pattern.finditer(text))

        return {
            "emails": list(emails),
            "phones": list(phones)
        }
    except Exception as e:
        return {"error": str(e)}

# url = "https://4kaglobal.com/"
# result = scrape_phone_email_turkish(url)
# print(result)
with open("data.csv", mode="r") as file:
    dataset = file.readlines()


names = []
urls = []
for data in dataset:
    cleaned_data = data.split(",")
    names.append(cleaned_data[0])
    urls.append(cleaned_data[1])

final_data = []
for index in range(1, len(urls)):
    result = scrape_phone_email_turkish(urls[index])
    print(result)
    if "emails" not in result:
        final_result = (names[index], [], [], urls[index])
    else:
        final_result = (names[index], result["emails"], result["phones"],  urls[index])
    print(final_result)
    final_data.append(final_result)
# print(final_data)
company_dataset = pd.DataFrame(final_data, columns=["Name", "Email", "Phone", "Url"])
# print(company_dataset)
company_dataset.to_csv("company_dataset", index=False)
company_dataset.to_excel("company_dataset.xlsx", index=False)
