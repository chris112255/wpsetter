#!/usr/bin/env python3

import urllib.request
import json
import sys
import ctypes
import os
import re
import shutil
import argparse

def set_wallpaper_reddit(subreddit = "wallpapers"):
    url = f"https://www.reddit.com/r/{subreddit}/.json?t=hot.json?limit=20"
    
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            while True:
                data = json.loads(response.read().decode())
                posts = data['data']['children']
                updated = False

                for post in posts:
                    img_url = post['data']['url']

                    if img_url.endswith(('.jpg', '.png', '.jpeg', 'gif')):
                        print(f"Checking: {img_url}")
                        name = post['data']['title']
                        name = re.sub(r'[^a-zA-Z ]', '', name)

                        home = os.path.expanduser("~")
                        folder_path = os.path.join(home, "Pictures", "scraped_wallpapers")
                        if not os.path.isdir(folder_path):
                            os.makedirs(folder_path)

                        file_path = os.path.join(folder_path, name+".jpeg")

                        if not os.path.exists(file_path):
                            updated = True
                            urllib.request.urlretrieve(img_url, file_path)
                            
                            ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)
                            break

                if updated: print("updated!")
                else: print("no update...")
                break
    except Exception as e:
        print(f"Failed: {e}")

def clean():
    home = os.path.expanduser("~")
    file_path = os.path.join(home, "Pictures", "scraped_wallpapers")
    shutil.rmtree(file_path)
    os.makedirs(file_path)
    print("cleaned!")

def main():
    parser = argparse.ArgumentParser(description="Wallpaper Setter")
    parser.add_argument("--r", type=str, default="wallpaper", help="The subreddit to pull from")
    parser.add_argument("--clean", action="store_true", help="Delete wallpapers saved")
    args = parser.parse_args()

    if args.clean: clean()
    set_wallpaper_reddit(args.r)