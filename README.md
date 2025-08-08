#  G2 Review Scraper

A robust Python-based scraper to extract product reviews and ratings from [G2.com](https://www.g2.com) using `Selenium` and `undetected-chromedriver`. Designed to bypass anti-bot detection and save reviews into structured JSON files.

---

## =====

- Scrapes real user reviews from G2
- Handles multiple pages 
- Extracts:
  - Review title
  - Review content
  - Rating
  - Review date
- JSON output saved locally

---
## while running you must Activate your virtual environment:
source .venv/bin/activate

## for running g2 scraper we has to run 
python test_g2.py


## Requirements

- Python 3.8+
- Google Chrome (latest)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with your Chrome version

Install dependencies:

```bash
pip install -r requirements.txt


