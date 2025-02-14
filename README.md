# Twitch Bot

## Overview
A Twitch chat bot that interacts with a streamer's (Synn) chat using a web scraper. It reads messages, detects specific triggers, and automatically participates in raffles. The bot uses **undetected_chromedriver** and **BeautifulSoup** to scrape the chat and interact using **pyautogui**.

## Features
- Reads Twitch chat messages in real time
- Detects messages from StreamElements and splits them accordingly
- Identifies specific trigger words to enter raffles automatically
- Sends a greeting message upon startup
- Refreshes the Twitch chat page after entering a raffle to ensure updated messages

## Technologies Used
- **Python**
- **undetected_chromedriver** (Bypasses bot detection in browsers)
- **BeautifulSoup** (Parses the chat messages)
- **PyAutoGUI** (Automates keyboard inputs)

## Installation

### Prerequisites
Make sure you have Python installed. You can install the required dependencies using:

```sh
pip install -r requirements.txt
