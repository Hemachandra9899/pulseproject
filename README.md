# G2 Review Scraper

A powerful Python-based web scraper designed to extract product reviews and ratings from [G2.com](https://www.g2.com). Utilizing `Selenium` and `undetected-chromedriver`, this tool effectively bypasses anti-bot detection and saves the extracted reviews in structured JSON format.

---

## Features

- Scrapes authentic user reviews from G2
- Supports pagination for comprehensive data collection
- Extracts the following information:
    - Review Title
    - Review Content
    - Rating
    - Review Date
- Saves output in JSON format locally

---
## I’ve built an interface that allows users to view reviews fetched by our scraper, organized by company name. The reviews are stored in a structured JSON file format.Run this and view the interface
- index.html 

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Chrome (latest version)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with your Chrome version

### Setup

1. **Clone the repository:**
     ```bash
     git clone <repository-url>
     cd pulse_scraper
     ```

2. **Activate your virtual environment:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```
4. **if access blocked reinstall :**
     ```bash
     pip install undetected-chromedriver beautifulsoup4
     ```
4. **Running:**
     ```bash
     python test_g2.py
     ```

### Running the Scraper

To run the G2 review scraper, execute the following command:

