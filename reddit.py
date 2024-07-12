import praw
import requests
import os
import argparse
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def parse_args():
    parser = argparse.ArgumentParser(description='Download all images posted by a specific Reddit user.')
    parser.add_argument('username', help='Reddit username whose images you want to download')
    parser.add_argument('--threads', type=int, default=20, help='Number of threads to use (default: 20)')
    parser.add_argument('--folder', default='downloaded_images', help='Folder to save images (default: "downloaded_images")')
    return parser.parse_args()

def is_image_url(url):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    return url.lower().endswith(image_extensions)

def download_image(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder, exist_ok=True)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.headers['Content-Type'].startswith('image'):
            ext = response.headers['Content-Type'].split('/')[1]
            filename = os.path.basename(urlparse(url).path)
            file_path = os.path.join(dest_folder, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {file_path}")
        else:
            print(f"Failed to download {url}: Non-image or bad status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def scrape_user_images(username, max_threads, dest_folder):
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='script:photo_scraper:v1.0 (by /u/YOUR_USERNAME)',
        username='YOUR_REDDIT_USERNAME',
        password='YOUR_REDDIT_PASSWORD'
    )
    
    user = reddit.redditor(username)
    images = [submission.url for submission in user.submissions.new(limit=None) if is_image_url(submission.url)]
    
    print(f"Found {len(images)} images to download.")
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(download_image, url, dest_folder): url for url in images}
        for future in as_completed(futures):
            url = futures[future]
            try:
                future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')

if __name__ == '__main__':
    args = parse_args()
    scrape_user_images(args.username, args.threads, args.folder)
