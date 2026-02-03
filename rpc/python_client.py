#!/usr/bin/env python3
"""
Simple XML-RPC client for testing the RPC server.

Usage:
    python3 python_client.py --host 127.0.0.1 --port 8000

"""
import argparse
import logging
import xmlrpc.client


def main():
    parser = argparse.ArgumentParser(description="Simple XML-RPC client")
    parser.add_argument("--host", default="127.0.0.1", help="Server host")
    parser.add_argument("--port", type=int, default=8000, help="Server port")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    url = f"http://{args.host}:{args.port}/RPC2"
    logging.info(f"Connecting to {url}")
    try:
        proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
        print("add(2,3) ->", proxy.add(2, 3))
        print("multiply(3.5,2) ->", proxy.multiply(3.5, 2))
        print("echo('hello') ->", proxy.echo('hello'))
        print("get_time() ->", proxy.get_time())
    except Exception as e:
        logging.exception("RPC client error")


if __name__ == "__main__":
    main()
