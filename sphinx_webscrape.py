import os
import requests
import json
import datetime

# File paths for tracking reported bounties and the last run timestamp
REPORTED_BOUNTIES_FILE = 'reported_bounties.txt'
LAST_RUN_FILE = 'last_run.txt'

def read_last_run_timestamp():
    try:
        with open(LAST_RUN_FILE, 'r') as file:
            return datetime.datetime.fromisoformat(file.read().strip())
    except (FileNotFoundError, ValueError):
        return None

def write_last_run_timestamp():
    with open(LAST_RUN_FILE, 'w') as file:
        file.write(datetime.datetime.now().isoformat())

def scrape_bounties(last_run_timestamp=None):
    url = "https://community.sphinx.chat/gobounties/all?limit=100&sortBy=created&search=&page=1&resetPage=true&Open=false&Assigned=false&Paid=false&languages="
    response = requests.get(url)

    bounty_details = []
    
    if response.status_code < 300:
        jsonObject = response.json()
        for bounty in jsonObject:
            posted_time = datetime.datetime.fromisoformat(bounty['bounty']['created'])
            if (not last_run_timestamp or posted_time > last_run_timestamp) and not bounty['bounty']['paid']:
                bounty_details.append({
                    "description": bounty['bounty']['description'],
                    "price": bounty['bounty']['price'],
                    "url": f"https://community.sphinx.chat/bounty/{bounty['bounty']['id']}",
                })
    return bounty_details

def post_to_discord(bounty_details, webhook_url):
    headers = {'Content-Type': 'application/json'}
    for bounty in bounty_details:
        embed = {
            "title": "🚀 New Bounty Alert!",
            "description": bounty['description'],
            "color": 5814783,
            "fields": [
                {"name": "💰 Value", "value": f"{bounty['price']} SAT", "inline": True},
                {"name": "🔗 URL", "value": bounty['url'], "inline": False}
            ],
            "footer": {"text": "Check out the new bounties and earn SATs!"}
        }
        payload = {"embeds": [embed]}
        response = requests.post(webhook_url, json=payload, headers=headers)
        
        if response.status_code == 204:
            print("Successfully posted to Discord.")
        else:
            print(f"Failed to post to Discord: {response.status_code}")
        time.sleep(1)

def main():
    last_run_timestamp = read_last_run_timestamp()
    bounty_details = scrape_bounties(last_run_timestamp)
    if bounty_details:
        webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
        if not webhook_url:
            raise EnvironmentError("The DISCORD_WEBHOOK_URL environment variable is not set.")
        post_to_discord(bounty_details, webhook_url)
        write_last_run_timestamp()
    else:
        print("No new unpaid bounties found.")

if __name__ == "__main__":
    main()
