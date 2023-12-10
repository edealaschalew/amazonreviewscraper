from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from textblob import TextBlob
import re
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random



def check_url(url):
    pattern1 = r"amazon\.com/.+/product-reviews/.+/" 
    pattern2 = r"amazon\.com/.+/dp/.+"

    match1 = re.fullmatch(pattern1, url)
    if match1:
        return url
    
    match2 = re.fullmatch(pattern2, url)
    if match2:
        product_name = url.split("/dp/")[0]
        product_id = url.split("/dp/")[1].split("/")[0]
        new_url = f"{product_name}/product-reviews/{product_id}/"
        return new_url

    return False
# Path to your web driver executable
driver_path = '/path/to/chromedriver'

# Set up options for a headless browser  
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  
chrome_options.add_argument(f'--user-agent={user_agent}')
# Create a new instance of the Chrome driver with headless options
driver = webdriver.Chrome(options=chrome_options)
def scrape(url):

    # if not check_url(url):
    #     print('Invalid Url')
    #     print(url)
    #     exit()
    
    print(url)
    driver.get(url)

    # Wait for page to load
    driver.implicitly_wait(5)

    all_reviews = []
    last_review = None

    def extract_reviews():
        reviews = []
        for x in range(1, 11):
            try:
                review = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{x}]/div/div/div[4]/span/span')
                reviews.append(review)
            except:
                pass
        return reviews

    while True:
        new_reviews = extract_reviews()

        if new_reviews:
            try:
                if last_review != new_reviews[-1].text:
                    for review in new_reviews:
                        # print(review.text)
                        all_reviews.append(review)
                    last_review = new_reviews[-1].text
                else:
                    break
            except:
                break
                
        next_btn = driver.find_element(By.XPATH, '//li[@class="a-last"]/a')
        next_btn.click()
        driver.implicitly_wait(5)

        # Re-initialize the reviews after navigating to the next page
        all_reviews = extract_reviews()
        


    reviews = {}


    for review in all_reviews:

        review_text = review.text
        # print(review_text)

        # Analyze sentiment using TextBlob
        sentiment = TextBlob(review_text).sentiment

        # Classify sentiment based on polarity score
        if sentiment.polarity > 0:
            sentiment_label = "Positive"
        elif sentiment.polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        
        reviews[review_text]=sentiment_label

    return reviews


reviews =scrape('https://www.amazon.com/Weierpidan-Sweatpants-Patchwork-Streetwear-Trousers/product-reviews/B0BM5W7CC2/')
print(reviews)
driver.quit()