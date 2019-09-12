#!/usr/bin/env bash
QUAY_USER=""
QUAY_PASS=""

sudo docker build -t color .
sudo docker tag color:latest quay.io/$QUAY_USER/color:latest
sudo docker push quay.io/$QUAY_USER/color:latest
