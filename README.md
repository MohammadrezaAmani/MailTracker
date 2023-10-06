# 💌 FastAPI Mail Tracker

![Project Logo](./tracker/assets/media/logo.jpg)

## Introduction

Python Mail Tracker is a powerful tool for tracking emails and website views, providing detailed information such as IP addresses, locations, headers, devices, browsers, timestamps, and more. This FastAPI-based application is designed to help you monitor and analyze user interactions with your emails or website, giving you valuable insights into user behavior.

## Features

- Track emails and website views with ease.
- Collect comprehensive information about each interaction.
- Analyze user data to improve your communication and website content.
- FastAPI backend for high-performance tracking.
- Easy-to-use API for integrating tracking into your applications.

## Table of Contents

- [💌 Python Mail Tracker](#-python-mail-tracker)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Usage](#usage)
    - [API Documentation](#api-documentation)
    - [Configuration](#configuration)
    - [Contributing](#contributing)
    - [License](#license)

## Installation

To get started with Python Mail Tracker, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/MohammadrezaAmani/MailTracker.git
cd MailTracker
```
1- Install the required dependencies:
```bash
pip install -r requirements.txt
```

1. Configure your settings (see Configuration below).

2. Run the FastAPI application:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
### Usage
Once you have the application up and running, you can start tracking emails or website views by making API requests. Here's a basic example of how to track an email:

```python
import requests

# Replace with your server's address
base_url = 'http://localhost:8000'

# Track an email
response = requests.post(f'{base_url}/track/email', json={
    'recipient_email': 'recipient@example.com',
    'email_subject': 'Important News',
    'email_content': 'Check out our latest newsletter!',
})

print(response.json())
```
For more advanced usage and API endpoints, please refer to the API Documentation section below.

### API Documentation
For detailed information on available API endpoints and how to use them, please check the API Documentation.

### Configuration
To customize the behavior of Python Mail Tracker, you can edit the config.py file. Here, you can configure database settings, logging, and other application-specific options.

### Contributing
We welcome contributions to make Python Mail Tracker even better! If you'd like to contribute, please follow our Contribution Guidelines.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
