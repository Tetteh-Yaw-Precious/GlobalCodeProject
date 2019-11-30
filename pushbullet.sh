#!/bin/bash

API="o.HohBGyYVQkUuHdUjSQLaQRTjfWQfP3Yj"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Alert" -d body="$MSG"

2.import os

3.Push Message :- 
os.system('/home/pi/program/pushbullet.sh "Alert Motion Detected"')
   