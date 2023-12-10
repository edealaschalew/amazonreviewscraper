# amazonreviewscraper
Amazon Reviews Scraper

This Python script utilizes Selenium and TextBlob to scrape and analyze product reviews from Amazon. The script is designed to work with Amazon product review pages and provides sentiment analysis for each review.

Key Features:

Seamless handling of Amazon product review URLs.
Headless browsing with a randomly generated user-agent for web scraping.
Extraction of reviews and continuous pagination support.
Sentiment analysis using TextBlob to classify reviews as Positive, Negative, or Neutral.
Dependencies:

selenium: Web scraping library for browser automation.
textblob: Natural Language Processing library for sentiment analysis.
fake_useragent: Library to generate random user agents for web scraping.
Usage:

Ensure you have the required dependencies installed (pip install selenium textblob fake_useragent).
Set the path to your ChromeDriver executable (driver_path variable).
Run the script, providing an Amazon product review URL as an argument to the scrape function.
python
Copy code
reviews = scrape('https://www.amazon.com/example-product-reviews/')
print(reviews)
Note:

The script is designed to work with Chrome. Make sure to download the appropriate ChromeDriver for your system and update the driver_path variable accordingly.
