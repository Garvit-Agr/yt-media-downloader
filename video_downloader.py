import os
import yt_dlp

# ──────────────────────────────────────────────────────────────
# VIDEO QUALITY SETTING
# ──────────────────────────────────────────────────────────────
# Change this value to set the maximum video resolution.
# Options:  360  |  480  |  720  |  1080  |  "best"
#
# Examples:
#   VIDEO_QUALITY = 360       # Low quality, smallest file size
#   VIDEO_QUALITY = 480       # Standard definition
#   VIDEO_QUALITY = 720       # HD (default, good balance)
#   VIDEO_QUALITY = 1080      # Full HD
#   VIDEO_QUALITY = "best"    # Highest available (may be 4K)
#
# Note: The quality setting is a maximum cap, not a guarantee.
# If you set 1080 but the video's best available is 480p,
# yt-dlp will download 480p — no error, no failure.
# ──────────────────────────────────────────────────────────────
VIDEO_QUALITY = 720

# ──────────────────────────────────────────────────────────────
# OUTPUT FOLDER NAME
# ──────────────────────────────────────────────────────────────
# Change this to set the name of the folder where downloaded
# MP4 files will be saved. The folder is created automatically
# in the same directory as this script.
# ──────────────────────────────────────────────────────────────
OUTPUT_FOLDER_NAME = 'Downloaded_Videos'


def download_videos(text_file):
    # Ensure the songs file exists
    if not os.path.exists(text_file):
        print(f"Error: {text_file} not found!")
        return

    # Read the URLs
    with open(text_file, 'r') as file:
        links = [line.strip() for line in file if line.strip()]

    if not links:
        print("Your links.txt file is empty.")
        return

    print(f"Found {len(links)} entries in your text file. Starting processing...\n")

    # Get the current directory where this script is running
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the output folder inside your current directory
    output_folder = os.path.join(current_directory, OUTPUT_FOLDER_NAME)

    # Build the format selector based on VIDEO_QUALITY
    if VIDEO_QUALITY == "best":
        format_selector = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    else:
        format_selector = (
            f'bestvideo[height<={VIDEO_QUALITY}][ext=mp4]+bestaudio[ext=m4a]/'
            f'best[height<={VIDEO_QUALITY}][ext=mp4]/'
            f'best[height<={VIDEO_QUALITY}]'
        )

    # yt-dlp Configuration
    ydl_opts = {
        'format': format_selector,
        'ignoreerrors': True,          # Essential for playlists: skips deleted/private videos instead of crashing
        'merge_output_format': 'mp4',  # Ensure final output is always MP4
        # Saves files inside the 'Downloaded_Videos' folder in your current workspace
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }

    # Execute download loop
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for index, link in enumerate(links, start=1):
            try:
                print(f"--- Processing Entry [{index}/{len(links)}]: {link} ---")
                ydl.download([link])
            except Exception as e:
                print(f"Error handling entry {link}: {e}")

    print(f"\n🎬 All tasks processed! Check your new folder here: {output_folder}")


if __name__ == '__main__':
    download_videos('links.txt')
