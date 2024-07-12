# Reddit Image Scraper

The "Reddit Image Scraper" is a Python tool designed to download all images posted by a specified Reddit user. It uses PRAW and the Requests library to automate image retrieval from a user's Reddit submissions. The script supports customization of download threads and destination folders via command-line arguments.
This tool downloads all images posted by a specified Reddit user.

## Requirements

- Python 3
- PRAW (Python Reddit API Wrapper)
- Requests library

## Setup

1. Install Python 3 and pip (Python package installer).
2. Install the required packages:

```
pip install praw requests
```

3. Register a Reddit application at https://www.reddit.com/prefs/apps to get your `client_id` and `client_secret`.
4. Update the script `reddit_image_scraper.py` with your Reddit application details and Reddit account credentials.
5. Configure the Script: Fill in your Reddit API credentials (`client_id`, `client_secret`, `user_agent`, `username`, and `password`) directly into the script. 

## Register a Reddit Application
1. Go to https://www.reddit.com/prefs/apps
2. Scroll down to the bottom and click on "Create App" or "Create Another App".
3. Fill in the details:
- Name: Your app’s name.
- Application Type: Choose "script".
- Description: Provide a brief description.
- About URL: You can leave this blank.
- Permissions: Set to "read".
- Redirect URI: http://localhost:8080 (standard for local testing)
5. Click "Create app".

## Usage

Run the script from the command line, specifying the Reddit username and optionally the number of threads and the folder to save images:

```
python reddit.py username --threads 20 --folder downloaded_images
```


### Arguments

- `username`: The Reddit username whose images you want to download.
- `--threads` (optional): Number of threads to use for downloading images. Default is 20.
- `--folder` (optional): Folder to save the downloaded images. Default is "downloaded_images".

## Note

This tool is intended for educational purposes and should be used in accordance with Reddit's API usage policies.
