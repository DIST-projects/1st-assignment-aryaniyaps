#!/usr/bin/env python3
"""
Simple seeder using libtorrent.

Usage:
    python3 seeder.py --torrent file.torrent --file path/to/shared/file
"""
import argparse
import libtorrent as lt
import time


def seed(torrent_path, file_path):
    ses = lt.session()
    ses.listen_on(6881, 6891)
    info = lt.torrent_info(torrent_path)
    params = {"save_path": ".", "storage_mode": lt.storage_mode_t.storage_mode_sparse, "ti": info}
    h = ses.add_torrent(params)
    print(f"Seeding {file_path} with infohash: {info.info_hash()}" )
    try:
        while True:
            s = h.status()
            print(f"state: {s.state}, seeds: {s.num_seeds}, peers: {s.num_peers}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping seeder")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--torrent", required=True)
    parser.add_argument("--file", required=True)
    args = parser.parse_args()
    seed(args.torrent, args.file)


if __name__ == "__main__":
    main()
