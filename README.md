# 🎵 yt-media-downloader

A dead-simple pair of Python scripts to bulk-download audio (MP3) or video (MP4) from YouTube — one link per line, supports both individual videos and entire playlists. Completely vibe coded.

---

## 📁 Repository Structure

```
yt-media-downloader/
├── README.md
├── audio_downloader.py     # YouTube → MP3 (configurable bitrate)
└── video_downloader.py     # YouTube → MP4 (configurable resolution)
```

---

## ⚙️ Prerequisites

1. **Python 3.11+**
2. **uv** — fast Python package manager ([install guide](https://docs.astral.sh/uv/getting-started/installation/))
   ```bash
   # Install uv (if you don't have it)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. **yt-dlp** — the download engine
   ```bash
   uv add yt-dlp
   ```
4. **FFmpeg** — required for audio extraction (MP3) and video merging (MP4)
   - **macOS:** `brew install ffmpeg`
   - **Ubuntu/Debian:** `sudo apt install ffmpeg`
   - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your system PATH

---

## 🚀 Usage

### Step 1 — Prepare your links

Create a file named **`links.txt`** in the **same directory** as the scripts. Add the URLs you want to download, with **one URL per line**:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=9bZkp7q19f0
```

> **💡 You can add either a single video URL or an entire playlist URL — the scripts handle both automatically.**
>
> If a playlist link is provided, every video in that playlist will be downloaded.

> **⚠️ Want to download your own playlist? Make sure it is set to Public (or Unlisted) first — private playlists cannot be accessed by the downloader.**

### Step 2 — Run a script

**Download as MP3 (audio only):**
```bash
uv run audio_downloader.py
```
Downloaded files are saved to a `Downloaded_Tracks/` folder created automatically in the script's directory.

**Download as MP4 (video):**
```bash
uv run video_downloader.py
```
Downloaded files are saved to a `Downloaded_Videos/` folder created automatically in the script's directory.

---

## 🎧 Audio Quality Configuration

Open `audio_downloader.py` and edit the `AUDIO_QUALITY` variable at the top:

```python
# Options:  128  |  192  |  256  |  320
AUDIO_QUALITY = 320   # ← Change this value
```

| Value | Bitrate | Notes |
|-------|---------|-------|
| `128` | 128 kbps | Low quality, smallest file size |
| `192` | 192 kbps | Good quality, balanced size |
| `256` | 256 kbps | High quality |
| `320` | 320 kbps *(default)* | Maximum MP3 quality |

> **Note:** If the source audio's actual bitrate is lower than your setting, the file will be encoded at the source's bitrate — no quality is artificially inflated.

---

## 🎬 Video Quality Configuration

Open `video_downloader.py` and edit the `VIDEO_QUALITY` variable at the top:

```python
# Options:  360  |  480  |  720  |  1080  |  "best"
VIDEO_QUALITY = 720   # ← Change this value
```

| Value | Resolution | Notes |
|-------|------------|-------|
| `360` | 360p | Low quality, smallest file size |
| `480` | 480p | Standard definition |
| `720` | 720p *(default)* | HD — good balance of quality & size |
| `1080` | 1080p | Full HD |
| `"best"` | Highest available | Could be 4K depending on the source |

> **Note:** The quality setting is a **maximum cap**, not a guarantee. If you set `1080` but the video's highest available resolution is 480p, yt-dlp will automatically download at 480p — no error, no failure. It always grabs the best available quality up to your limit.

---

## 📝 Notes

- **Playlists with private/deleted videos** — The scripts will automatically skip unavailable videos and continue downloading the rest.
- **File naming** — Files are saved using the video's YouTube title. Duplicates in the same folder will be overwritten.
- **`links.txt` is not included** in this repo — you create it yourself with your own links.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⚠️ Disclaimer

This tool is intended for **personal and educational use only**. Downloading copyrighted content without permission may violate [YouTube's Terms of Service](https://www.youtube.com/static?template=terms) and copyright laws in your jurisdiction. The authors are not responsible for any misuse of this software. Please respect content creators' rights.
