
import json
from g2_scraper import scrape_g2_reviews

PRODUCT_SLUG = "facebook"
MAX_PAGES = 5
OUTPUT_FILE = f"{PRODUCT_SLUG}_g2_reviews.json"

if __name__ == "__main__":
    reviews = scrape_g2_reviews(PRODUCT_SLUG, MAX_PAGES)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Collected {len(reviews)} reviews")
    print(f"📦 Saved to {OUTPUT_FILE}")
