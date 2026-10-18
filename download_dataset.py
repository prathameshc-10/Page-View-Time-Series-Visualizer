"""Download the freeCodeCamp forum page-views dataset."""
from pathlib import Path
from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/main/fcc-forum-pageviews.csv"
OUTPUT = Path(__file__).with_name("fcc-forum-pageviews.csv")


def main():
    if OUTPUT.exists() and OUTPUT.stat().st_size > 0:
        print(f"Dataset already exists: {OUTPUT.name}")
        return
    print("Downloading page-view dataset...")
    with urlopen(URL, timeout=30) as response:
        data = response.read()
    OUTPUT.write_bytes(data)
    print(f"Saved {len(data):,} bytes to {OUTPUT.name}")


if __name__ == "__main__":
    main()
