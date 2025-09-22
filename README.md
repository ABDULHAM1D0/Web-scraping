# 🕸️ Web Scraper – Company Contact Info Extractor
## 📖 Project Overview
This project is a web scraping tool that helps you quickly collect company contact details from the web.

### Input: A company name

### Process:
- Finds the first official website URL for that company.
- Scrapes the phone number and email address from that website.
### Output: The extracted information is displayed and can be saved for further use

### This tool is useful for market research, lead generation, and business analysis.

## 🚀 Features
- 🔎 Automatically searches for the official company website.
- 📬 Extracts email addresses.
- ☎️ Extracts phone numbers.
- 💾 Option to save results (e.g., Excel, CSV, JSON).
- 🛡️ Handles missing data gracefully.
- ⚙️ Installation.

## Install dependencies:

```bash
pip install -r requirements.txt
```

## ⚠️ Notes
- The scraper works best with well-structured websites.
- Some websites may block scraping → consider adding headers, retries, or proxies.
- Always respect websites’ robots.txt and scraping policies.

## 🛠️ Technologies Used
- Python
- Requests / Playwright / Selenium (depending on implementation).
- BeautifulSoup / lxml for parsing.
- pandas for saving structured data.

## 📌 Next Steps / Improvements
- Add multi-company batch scraping.
- Improve error handling.
- Extract additional info (e.g., address, social media links).
- Implement a GUI or web interface.
