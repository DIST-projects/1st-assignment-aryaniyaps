#!/usr/bin/env python3
"""
Create a simple .torrent file using libtorrent Python bindings.

Usage:
    python3 create_torrent.py --file path/to/file --tracker udp://tracker.openbittorrent.com:80

This script will also write a `.sha1` file next to the input file with the full-file SHA1.
"""
import argparse
import hashlib
import libtorrent as lt
import time


def sha1_of_file(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def create_torrent(path, tracker, out):
    fs = lt.file_storage()
    lt.add_files(fs, path)
    t = lt.create_torrent(fs)
    t.add_tracker(tracker)
    t.set_creator("student-torrent-script")
    lt.set_piece_hashes(t, ".")
    torrent = t.generate()
    with open(out, "wb") as f:
        f.write(lt.bencode(torrent))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--tracker", default="udp://tracker.openbittorrent.com:80")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    out = args.out if args.out else args.file + ".torrent"
    print(f"Creating torrent for {args.file} -> {out}")
    create_torrent(args.file, args.tracker, out)
    sha1 = sha1_of_file(args.file)
    with open(args.file + ".sha1", "w") as f:
        f.write(sha1)
    print(f"Wrote {out} and SHA1: {sha1}")


if __name__ == "__main__":
    main()
