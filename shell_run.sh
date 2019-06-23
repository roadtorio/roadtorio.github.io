#!/bin/sh
cd /home/pi/Tokyo/roadtotokyo.github.io
#../venv/bin/python Data/DataGathering/main.py
#../venv/bin/python jinjify.py
git add .
git commit -m 'Automated Daily Commit'
git push
