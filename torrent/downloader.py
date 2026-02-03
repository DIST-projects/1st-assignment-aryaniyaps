#!/usr/bin/env python3
"""
Simple BitTorrent downloader using libtorrent.

Usage:
    python3 downloader.py --torrent file.torrent --out-dir downloads/

After download, if a `.sha1` file exists next to the content name, the script will verify SHA1.
"""
import argparse
import libtorrent as lt
import time
import os
import hashlib


def sha1_of_file(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def download(torrent_path, out_dir):
    ses = lt.session()
    ses.listen_on(6881, 6891)
    e = lt.bdecode(open(torrent_path, "rb").read())
    info = lt.torrent_info(e)
    params = {"save_path": out_dir, "storage_mode": lt.storage_mode_t.storage_mode_sparse, "ti": info}
    h = ses.add_torrent(params)
    print(f"Started download, infohash: {info.info_hash()}")
    while not h.is_seed():
        s = h.status()
        print(f"progress: {s.progress * 100:.2f}%, peers: {s.num_peers}")
        time.sleep(2)
    print("Download complete")
    # verify sha1 if available
    # torrent contains file names, pick first file path
    file_entry = info.files().file_path(0)
    downloaded_path = os.path.join(out_dir, file_entry)
    sha1_path = downloaded_path + ".sha1"
    if os.path.exists(sha1_path):
        expected = open(sha1_path).read().strip()
        actual = sha1_of_file(downloaded_path)
        print(f"Expected SHA1: {expected}")
        print(f"Actual   SHA1: {actual}")
        if expected == actual:
            print("SHA1 matches: file integrity OK")
        else:
            print("SHA1 mismatch: file corrupted")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--torrent", required=True)
    parser.add_argument("--out-dir", default="downloads")
    args = parser.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    download(args.torrent, args.out_dir)


if __name__ == "__main__":
    main()
