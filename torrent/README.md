# Torrent Assignment

This folder contains simple Python scripts to create a `.torrent` file and to demonstrate seeding and downloading using `libtorrent`.

Files:

- `create_torrent.py` — create a `.torrent` from a file and optionally save a `.sha1` checksum file.
- `seeder.py` — starts a libtorrent session and seeds the file for other peers.
- `downloader.py` — downloads the file given the `.torrent` file and checks SHA1 if provided.

Requirements:

- Python 3.8+
- `libtorrent` (python binding). On Ubuntu: `sudo apt install python3-libtorrent` or use `pip` if available.

Notes:

- For testing locally you can use a public tracker like `udp://tracker.openbittorrent.com:80` or run a local tracker.
- Do not upload copyrighted files. Use small test files.
