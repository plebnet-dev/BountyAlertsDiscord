# BountyAlertsDiscord

"BountyAlertsDiscord" is a tool designed to send notifications about new bounty opportunities directly to Discord channels.

## Overview

This Python program automates the process of scraping web pages for bounty information and posting updates directly to Discord channels. It uses Selenium for web scraping to gather details about bounties from `https://community.sphinx.chat/bounties` and then pushes these updates to a specified Discord webhook.

## Features

- **Web Scraping**: Extracts bounty information, including author, description, price, currency, and URL.
- **Discord Integration**: Automatically posts bounty details to a Discord channel via webhooks.

## Requirements

- Python 3
- Selenium
- Requests

## Setup

1. Install dependencies: `pip install selenium requests`.
2. Update `chromedriver_path` with the path to your ChromeDriver.
3. Set your Discord webhook URL in `webhook_url`.

## Usage

Run the script with `python3 sphinx_webscrape.py`. Ensure your system has ChromeDriver installed and accessible.

## Contribution

Feel free to fork, modify, and make pull requests to improve the script or add new features.
