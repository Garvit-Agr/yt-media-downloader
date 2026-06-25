import os
import subprocess
import sys

# ──────────────────────────────────────────────────────────────
# AUDIO FORMAT SETTING
# ──────────────────────────────────────────────────────────────
# Change this value to set the output audio format.
# Options:  "mp3"  |  "m4a"  |  "flac"  |  "ogg"
#
# Examples:
#   AUDIO_FORMAT = "mp3"     # Most compatible
#   AUDIO_FORMAT = "m4a"     # Apple-friendly, good quality (default)
#   AUDIO_FORMAT = "flac"    # Lossless, largest file size
#   AUDIO_FORMAT = "ogg"     # Open-source format, good quality
# ──────────────────────────────────────────────────────────────
AUDIO_FORMAT = 'm4a'

# ──────────────────────────────────────────────────────────────
# AUDIO QUALITY SETTING
# ──────────────────────────────────────────────────────────────
# Change this value to set the audio bitrate.
# Options:  "128k"  |  "192k"  |  "256k"  |  "320k"  |  "disable"
#
# Examples:
#   AUDIO_QUALITY = "128k"      # Low quality, smallest file size
#   AUDIO_QUALITY = "192k"      # Good quality, balanced size
#   AUDIO_QUALITY = "256k"      # High quality
#   AUDIO_QUALITY = "320k"      # Maximum quality
#   AUDIO_QUALITY = "disable"   # No re-encoding, keeps source quality (default)
#
# Note: If the source audio's actual bitrate is lower than your
# setting, the file will be at the source's bitrate.
# No quality is artificially inflated.
# ──────────────────────────────────────────────────────────────
AUDIO_QUALITY = 'disable'

# ──────────────────────────────────────────────────────────────
# OUTPUT FOLDER NAME
# ──────────────────────────────────────────────────────────────
# Change this to set the name of the folder where downloaded
# tracks will be saved. The folder is created automatically
# in the same directory as this script.
# ──────────────────────────────────────────────────────────────
OUTPUT_FOLDER_NAME = 'Downloaded_Spotify'


def download_spotify(text_file):
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
    os.makedirs(output_folder, exist_ok=True)

    # Execute download loop using spotdl CLI
    for index, link in enumerate(links, start=1):
        try:
            print(f"--- Processing Entry [{index}/{len(links)}]: {link} ---")

            command = [
                sys.executable, '-m', 'spotdl',
                'download', link,
                '--output', output_folder,
                '--format', AUDIO_FORMAT,
                '--bitrate', AUDIO_QUALITY,
            ]

            result = subprocess.run(command, check=False)

            if result.returncode != 0:
                print(f"Warning: spotdl returned an error for {link}, continuing...\n")

        except Exception as e:
            print(f"Error handling entry {link}: {e}")

    print(f"\n🎶 All tasks processed! Check your new folder here: {output_folder}")


if __name__ == '__main__':
    download_spotify('links.txt')
