import json
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc


def setup_driver():

    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    return uc.Chrome(options=options)


def scrape_g2_reviews(product_slug: str, max_pages: int = 3):

    base_url = f"https://www.g2.com/products/{product_slug}/reviews?page="
    all_reviews = []

    driver = setup_driver()

    try:
        for page in range(1, max_pages + 1):
            url = base_url + str(page)
            print(f"🔍 Scraping page {page}: {url}")
            driver.get(url)
            time.sleep(10)  # Let the page load fully

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            review_articles = soup.find_all('article')

            if not review_articles:
                print("❌ No review cards found — possibly blocked or empty.")
                break

            for article in review_articles:
                try:
                    title = article.find('div', itemprop='name').text.strip()
                    body = article.find('div', itemprop='reviewBody').text.strip()
                    rating = article.find('meta', itemprop='ratingValue')['content']
                    author = article.find('meta', itemprop='name')['content']
                    date = article.find('meta', itemprop='datePublished')['content']

                    all_reviews.append({
                        'title': title,
                        'body': body,
                        'rating': rating,
                        'author': author,
                        'date': date
                    })

                except Exception as e:
                    print(f"⚠️ Error parsing review: {e}")
                    continue

            time.sleep(2)

    finally:
        driver.quit()

    return all_reviews
