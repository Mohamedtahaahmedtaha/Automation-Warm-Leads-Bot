# Warm Lead Generation Bot

### Overview
This project implements a fully automated **AI-powered lead generation system** that scans Reddit job and freelance communities, identifies "warm leads" (users looking to hire or purchase tech services), and logs them into a Google Sheet while notifying via Telegram.

It is the **mandatory project (75%)** for the Sofindex AI Automation Engineer practical assessment.


### Core Functionality
- Scrapes recent posts from relevant Reddit subreddits.
- Uses an **AI model** (`gpt-4o-mini` via OpenRouter) to analyze each post.
- Classifies posts as *warm leads* based on hiring or buying intent.
- Saves qualified leads to **Google Sheets** with timestamp, subreddit, link, summary, and confidence score.
- Sends **Telegram alerts** for high-confidence leads.



### Tech Stack
- **Language:** Python 3.10+
- **APIs:** Reddit (PullPush API), OpenRouter (LLM), Telegram Bot API, Google Sheets API
- **Libraries:**  
  `requests`, `json`, `time`, `logging`, `gspread`, `tqdm`, `google.oauth2`, `datetime`



### Folder Structure
│
├── warm_lead_bot.py # main application script
├── credentials.json # Google service account credentials
├── requirements.txt # list of dependencies
├── warm_lead_bot.log # runtime logs
└── README.md # documentation

### 🔧 Environment Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
2. Set Up Google Sheets API

Create a Google Cloud project.

Enable “Google Sheets API” and “Google Drive API”.

Generate a service account key (credentials.json).

Share your target Google Sheet with the service account email.

Configure Variables
Edit the configuration section in warm_lead_bot.py:

openrouter_key = "YOUR_OPENROUTER_API_KEY"
telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
telegram_chat_id = "YOUR_CHAT_ID_OR_GROUP_ID"
sheet_name = "Warm Leads"

Telegram Notification Example
New Warm Lead!

Subreddit: forhire
Title: Hiring Python Developer for Web Project
Confidence: 91.0%
Summary: Client is seeking a freelance developer to build a web app.
[View Post](https://reddit.com/r/forhire/xxxxxx)

Customization Options

You can easily modify:

lead_threshold / alert_threshold → Adjust how strict the lead detection is.

Subreddits list → Add or remove target communities.

Model name → Swap gpt-4o-mini for other OpenRouter models.

Telegram broadcast → Add multiple chat IDs for notifications.

Logging

All activity is logged in:

warm_lead_bot.log

Includes:

Fetching status

API response issues

Leads saved

Telegram alert results

### Summary

This system demonstrates:

Real-world automation using AI + APIs

Reliable asynchronous error handling

Integration across Reddit, OpenRouter, Google Sheets, and Telegram

Production-level code quality and modular design

Author: Mohamed Taha
Date: October 2025
