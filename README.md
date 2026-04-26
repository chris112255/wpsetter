# reddit-wallpaper-setter-
A lightweight Python CLI tool that automatically updates your desktop wallpaper on startup using the latest high-resolution images from your favorite subreddits.

## Features
Subreddit Customization: Pull images from any subreddit (e.g., r/EarthPorn, r/Wallpapers).

Automated Startup: Designed to run invisibly in the background on system boot.

## Installation
The recommended way to install wpsetter is via pipx. This installs the tool in an isolated environment while making the command available globally.

Install via pipx:

```bash
pipx install git+https://github.com/chris112255/reddit-wallpaper-setter-.git
```

## Usage
### Manual Refresh
Change your wallpaper on demand by specifying a subreddit:

```bash
wpsetter --subreddit EarthPorn
```

### Background Automation (Windows)
Add the script into Task Scheduler.

## License
MIT
