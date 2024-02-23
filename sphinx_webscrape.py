import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

def scrape_bounties(driver):
    url = 'https://community.sphinx.chat/bounties'
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)  # Adjust timeout as needed
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.DescriptionContainer")))  # Ensure this waits for a reliably present element

    bounty_details = []

    bounty_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='description-price-container']")  # Update this selector based on your page structure

    for bounty in bounty_elements:
        try:
            author = bounty.find_element(By.CSS_SELECTOR, "div.sc-pzMyG.dnxgfw").text
        except Exception:
            author = "Unknown"  # Default value in case of an error

        try:
            href = bounty.find_element(By.CSS_SELECTO,"a").get_attribute('href')
            url = f"https://community.sphinx.chat{href}" 
        except Exception:
            url = "Unknown"  # Default value in case of an error

        try:
            price = bounty.find_element(By.CSS_SELECTOR, "div[class*='Price_inner_Container'] div[class*='Price_Dynamic_Text']").text
        except Exception:
            price = "Unknown"  # Default value in case of an error

        try:
            currency = bounty.find_element(By.CSS_SELECTOR, "div[class*='Price_SAT_Container'] div[class*='Price_SAT_Text']").text
        except Exception:
            currency = "Unknown"  # Default value in case of an error

        try:
            posted_time = bounty.find_element(By.CSS_SELECTOR, "div.sc-pHIBf.eYPEZX").text
        except Exception:
            posted_time = "Unknown"  # Default value in case of an error

        try:
            description = bounty.find_element(By.CSS_SELECTOR, "div[class*='DescriptionContainer']").text
        except Exception:
            description = "Description not found"

        bounty_details.append({
            "author": author,
            "posted_time": posted_time,
            "description": description,
            "currency": currency,
            "price": price,
            "url" : url
        })

    return bounty_details

def post_to_discord(bounty_details, webhook_url):
    for bounty in bounty_details:
        message = f"{bounty.get('author', 'Unknown')} posted a bounty: {bounty.get('description', 'N/A')} {bounty.get('posted_time', 'N/A')} {bounty.get('price', 'N/A')} {bounty.get('currency', 'N/A')} {bounty.get('url', 'N/A')}"
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("Successfully posted to Discord.")
        else:
            print(f"Failed to post to Discord: {response.status_code}")

def main():
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
    if not chromedriver_path:
        raise EnvironmentError("The CHROMEDRIVER_PATH environment variable is not set.") 
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    try:
        bounty_details = scrape_bounties(driver)
        if bounty_details:
            webhook_url = 'https://discord.com/api/webhooks/1208452918156460073/YiNa5U_WdDdInOIVe9Q8SiowwAHpR_kHZ5mYySWVldcm9BybeUXd9eqLhZD-BpAfpLFt'
            post_to_discord(bounty_details, webhook_url)
        else:
            print("No bounty descriptions found.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
