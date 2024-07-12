# reddit_image_downloader
The "Reddit Image Scraper" is a Python tool designed to download all images posted by a specified Reddit user. It uses PRAW and the Requests library to automate image retrieval from a user's Reddit submissions. The script supports customization of download threads and destination folders via command-line arguments.

# Reddit Image Scraper

This tool downloads all images posted by a specified Reddit user.

## Requirements

- Python 3
- PRAW (Python Reddit API Wrapper)
- Requests library

## Setup

1. Install Python 3 and pip (Python package installer).
2. Install the required packages:

'''
pip install praw requests
'''

3. Register a Reddit application at https://www.reddit.com/prefs/apps to get your `client_id` and `client_secret`.
4. Update the script `reddit_image_scraper.py` with your Reddit application details and Reddit account credentials.

## Usage

Run the script from the command line, specifying the Reddit username and optionally the number of threads and the folder to save images:

'''
python reddit_image_scraper.py username --threads 20 --folder downloaded_images
'''


### Arguments

- `username`: The Reddit username whose images you want to download.
- `--threads` (optional): Number of threads to use for downloading images. Default is 20.
- `--folder` (optional): Folder to save the downloaded images. Default is "downloaded_images".

## Note

This tool is intended for educational purposes and should be used in accordance with Reddit's API usage policies.
