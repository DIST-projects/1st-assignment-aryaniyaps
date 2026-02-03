#!/usr/bin/env python3
"""
Simple XML-RPC server for Assignment 1 (student-style implementation).

Exposes a few simple remote procedures: add, multiply, echo, get_time.

Usage:
    python3 python_server.py --host 0.0.0.0 --port 8000

"""
import argparse
import logging
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import time


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def add(a, b):
    try:
        return int(a) + int(b)
    except Exception as e:
        logging.exception("add() error")
        raise


def multiply(a, b):
    try:
        return float(a) * float(b)
    except Exception as e:
        logging.exception("multiply() error")
        raise


def echo(msg):
    try:
        return f"ECHO: {str(msg)}"
    except Exception:
        logging.exception("echo() error")
        raise


def get_time():
    return time.ctime()


def serve(host: str, port: int):
    server = SimpleXMLRPCServer((host, port), requestHandler=RequestHandler, allow_none=True)
    server.register_introspection_functions()
    server.register_function(add, "add")
    server.register_function(multiply, "multiply")
    server.register_function(echo, "echo")
    server.register_function(get_time, "get_time")

    logging.info(f"RPC server listening on {host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server interrupted by user, shutting down")
    except Exception:
        logging.exception("Server error")
    finally:
        server.server_close()


def main():
    parser = argparse.ArgumentParser(description="Simple XML-RPC server")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    serve(args.host, args.port)


if __name__ == "__main__":
    main()
