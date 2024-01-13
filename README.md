# YouTube Playlist Downloader
## Overview

This Python script is designed to simplify the process of downloading all the playlists from a YouTube artist or any other YouTuber's channel. It uses multithreading to enhance the download speed and leverages Selenium with Chrome driver to automate the playlist retrieval process.

### Prerequisites

Before using this script, you need to have the following dependencies installed:

1. **Python**: Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **youtube-dl**: Install youtube-dl using pip by running the following command:

   ```
   pip install youtube-dl
   ```

3. **Selenium**: Install Selenium using pip by running the following command:

   ```
   pip install selenium
   ```

4. **Chrome WebDriver**: You need to download the Chrome WebDriver and ensure it's in your system's PATH. You can download it from the [official Chrome WebDriver page](https://sites.google.com/chromium.org/driver/).

### Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script with the following command:

   ```
   python youtube_playlist_downloader.py
   ```

4. The script will prompt you to enter the URL of the YouTube channel's playlist page you want to download. Paste the URL and press Enter.

5. The script will automatically fetch all the playlists from the provided channel's playlist page.

6. You can choose to download all playlists or select specific ones.

7. The script will then initiate a multithreaded download process, downloading each playlist in parallel.

### Configuration

You can configure the script using the following options in the `youtube_playlist_downloader.py` file:

- `OUTPUT_DIRECTORY`: You can specify the directory where the downloaded playlists will be saved.

- `MAX_THREADS`: You can adjust the maximum number of threads used for parallel downloading based on your system's capabilities.

### Disclaimer

This script is intended for personal use or educational purposes only. Ensure that you comply with YouTube's terms of service and copyright laws when using this script. Downloading copyrighted content without proper authorization may infringe on copyright regulations.

## License

This script is provided under the [MIT License](LICENSE), so feel free to modify and distribute it as needed.

## Acknowledgments

- This script uses the youtube-dl library for downloading YouTube playlists.

Enjoy downloading YouTube playlists with ease using this script! If you encounter any issues or have suggestions for improvements, please feel free to contribute or report them in the repository's issue section.
