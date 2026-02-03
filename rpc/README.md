# RPC (Python) Assignment

This folder contains a small XML-RPC server and client implemented in Python.

Files:

- `python_server.py` — XML-RPC server exposing simple functions (`add`, `multiply`, `echo`, `time`).
- `python_client.py` — CLI client to call remote procedures.

How to run locally:

1. Install Python 3.8+ (venv recommended).
2. From the `rpc` folder run the server:

```
python3 python_server.py --host 0.0.0.0 --port 8000
```

3. In another terminal run some calls:

```
python3 python_client.py --host 127.0.0.1 --port 8000
```

AWS notes:

- Launch an EC2 instance (Amazon Linux 2 or Ubuntu). Open inbound TCP ports `8000` (RPC) and `22` (SSH), and `1099` for RMI if you host RMI on EC2.
- Copy the `rpc/` folder to the instance, install Python, and run `python_server.py` as a background service (or use `screen` / `tmux`).
- Do not upload credentials; use SSH keys.
