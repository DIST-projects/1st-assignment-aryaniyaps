## Setup Guide

Clone/download files: Dockerfile, requirements.txt, app.py

Build image: docker build -t my-flask-app .

Run container: docker run -p 5000:5000 my-flask-app

Open browser: http://localhost:5000 → "Hello from Dockerized Python Flask!"

Launch EC2 Instance

Ubuntu 24.04 (free tier)

t2.micro (cheap!)

Security group: Allow port 5000 (HTTP too)

SSH & Setup

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
sudo apt update && sudo apt install docker.io -y
sudo usermod -aG docker ubuntu  # Logout/login
Deploy App
```

```bash
git clone your-repo  # Or scp files
cd project-folder
docker build -t flask-app .
docker run -d -p 5000:5000 --name myapp flask-app
Check it! → http://your-ec2-ip:5000
```