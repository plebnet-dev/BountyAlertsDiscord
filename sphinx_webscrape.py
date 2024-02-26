import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import requests
import json

def scrape_bounties2():
    url  = "https://community.sphinx.chat/gobounties/all?limit=100&sortBy=created&search=&page=1&resetPage=true&Open=false&Assigned=false&Paid=false&languages="
    x = requests.get(url)

    bounty_details = []
    
    if x.status_code < 300:
       jsonObject = json.loads(x.content)
       for bounty in jsonObject:
            bounty_details.append({
                "author": bounty['owner']['owner_alias'],
                "posted_time": bounty['bounty']['created'],
                "description": bounty['bounty']['description'],
                "currency": "SAT",
                "price": bounty['bounty']['price'],
                "url": f"https://community.sphinx.chat/bounty/{bounty['bounty']['id']}",
                "coding_languages": bounty['bounty']['coding_languages']
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
    bounty_details = scrape_bounties2()
    if bounty_details:
        webhook_url = os.getenv('webhook_url')  # Make sure this is set in your environment
        if not webhook_url:
            raise EnvironmentError("The webhook_url environment variable is not set.")
        post_to_discord(bounty_details, webhook_url)
    else:
        print("No bounty descriptions found.") 

if __name__ == "__main__": 
    main()
