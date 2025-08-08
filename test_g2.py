import json
from g2_scraper import scrape_g2_reviews

# Customize these values
product_slug = "facebook"  # example: 'facebook', 'figma', 'salesforce'
max_pages = 3
start_date = None  # Example: "2023-01-01" it will return if there are any reviews in the date range
end_date = None    # Example: "2023-12-31"

reviews = scrape_g2_reviews(
    product_slug=product_slug,
    max_pages=max_pages,
    start_date=start_date,
    end_date=end_date
)

print(f"\n✅ Collected {len(reviews)} reviews")

# Save to file
output_filename = f"{product_slug}_g2_reviews.json"
with open(output_filename, "w") as f:
    json.dump(reviews, f, indent=2)

print(f"📦 Saved to {output_filename}")
