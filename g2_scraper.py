import json
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    return uc.Chrome(options=options)


def is_within_date_range(review_date: str, start_date: str, end_date: str) -> bool:
    if not start_date and not end_date:
        return True
    try:
        review_dt = datetime.strptime(review_date, "%Y-%m-%d")
        if start_date:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            if review_dt < start_dt:
                return False
        if end_date:
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            if review_dt > end_dt:
                return False
        return True
    except ValueError:
        return False


def scrape_g2_reviews(product_slug: str, max_pages: int = 3, start_date=None, end_date=None):
    base_url = f"https://www.g2.com/products/{product_slug}/reviews?page="
    all_reviews = []

    driver = setup_driver()

    try:
        for page in range(1, max_pages + 1):
            url = base_url + str(page)
            print(f"🔍 Scraping page {page}: {url}")
            try:
                driver.get(url)
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.TAG_NAME, "article"))
                )
            except Exception as e:
                print(f"❌ Failed to load page: {e}")
                continue

            soup = BeautifulSoup(driver.page_source, "html.parser")
            review_articles = soup.find_all("article")
            print(f"📝 Found {len(review_articles)} reviews on page {page}")

            if not review_articles:
                print("❌ No review cards found — possibly blocked or empty.")
                break

            for article in review_articles:
                try:
                    title = article.find("div", itemprop="name").text.strip()
                    body = article.find("div", itemprop="reviewBody").text.strip()
                    rating = article.find("meta", itemprop="ratingValue")["content"]
                    author = article.find("meta", itemprop="name")["content"]
                    date = article.find("meta", itemprop="datePublished")["content"]

                    if is_within_date_range(date, start_date, end_date):
                        all_reviews.append({
                            "title": title,
                            "body": body,
                            "rating": rating,
                            "author": author,
                            "date": date
                        })

                except Exception as e:
                    print(f"⚠️ Error parsing review: {e}")
                    continue

            time.sleep(10)

    finally:
        driver.quit()

    return all_reviews
