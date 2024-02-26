# BountyAlertsDiscord

## Overview

BountyAlertsDiscord is a Python-based tool designed to automate the notification process for new bounty opportunities. By fetching information from a JSON API and posting updates directly to Discord channels, it streamlines the dissemination of bounty information to interested parties.

## Features

- **API Integration**: Fetches the latest bounty information, including author, description, price, currency, and URL.
- **Discord Integration**: Utilizes Discord webhooks to post updates automatically to a specified Discord channel.

## Requirements

- Python 3.x (Any version typically)
- Requests library

## Setup Instructions

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/BountyAlertsDiscord.git
   cd BountyAlertsDiscord
   ```

2. **Install Dependencies**

   Ensure Python 3.x is installed on your system. Install the required Python package:

   ```sh
   pip install requests
   ```

3. **Environment Configuration**

   Set the `DISCORD_WEBHOOK_URL` environment variable to your Discord webhook URL. This can be done by adding the following line to your `.bashrc`, `.zshrc`, or equivalent shell configuration file:

   ```sh
   export DISCORD_WEBHOOK_URL='your_webhook_url_here'
   ```

   Remember to replace `'your_webhook_url_here'` with your actual Discord webhook URL.

### Running the Script

Execute the script from the terminal:

```sh
python3 sphinx_webscrape.py
```

Ensure that the `DISCORD_WEBHOOK_URL` environment variable is correctly set in your environment before running the script. The script will fetch the latest bounty information and post updates to the specified Discord channel.

## Contributing

We welcome contributions to BountyAlertsDiscord! If you have suggestions for improvement or want to contribute code, please feel free to fork the repository, make your changes, and submit a pull request.

## Directory Structure

```
BountyAlertsDiscord/
├── LICENSE
├── README.md
└── sphinx_webscrape.py
```

- `LICENSE`: The full license text for the project.
- `README.md`: This document, providing an overview and setup instructions.
- `sphinx_webscrape.py`: The Python script that interfaces with the API and Discord webhooks.

```

Feel free to adjust the repository URL and any other specific details to match your project's setup.
```
