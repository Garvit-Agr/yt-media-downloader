import os
import yt_dlp

# ──────────────────────────────────────────────────────────────
# AUDIO QUALITY SETTING
# ──────────────────────────────────────────────────────────────
# Change this value to set the MP3 bitrate (in kbps).
# Options:  128  |  192  |  256  |  320
#
# Examples:
#   AUDIO_QUALITY = 128    # Low quality, smallest file size
#   AUDIO_QUALITY = 192    # Good quality, balanced size
#   AUDIO_QUALITY = 256    # High quality
#   AUDIO_QUALITY = 320    # Maximum quality (default)
#
# Note: If the source audio's actual bitrate is lower than your
# setting, the file will be encoded at the source's bitrate.
# No quality is artificially inflated.
# ──────────────────────────────────────────────────────────────
AUDIO_QUALITY = 320

# ──────────────────────────────────────────────────────────────
# OUTPUT FOLDER NAME
# ──────────────────────────────────────────────────────────────
# Change this to set the name of the folder where downloaded
# MP3 files will be saved. The folder is created automatically
# in the same directory as this script.
# ──────────────────────────────────────────────────────────────
OUTPUT_FOLDER_NAME = 'Downloaded_Tracks'


def download_music(text_file):
    # Ensure the links file exists
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

    # yt-dlp Configuration
    ydl_opts = {
        'format': 'bestaudio/best',
        'ignoreerrors': True,         # Essential for playlists: skips deleted/private videos instead of crashing
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',               # Output format
            'preferredquality': str(AUDIO_QUALITY), # MP3 bitrate from config above
        }],
        # Saves files inside the 'Downloaded_Tracks' folder in your current workspace
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

    print(f"\n🎉 All tasks processed! Check your new folder here: {output_folder}")


if __name__ == '__main__':
    download_music('links.txt')