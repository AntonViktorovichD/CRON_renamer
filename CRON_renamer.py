#!/usr/bin/python3

import os

for filename in os.listdir('/home/grand/web/grandgold.jewelry/public_html/bitrix/backup'):
    if filename.find('grandgold.jewelry_') != -1:
        os.rename(f'/home/grand/web/grandgold.jewelry/public_html/bitrix/backup/{filename}', f'/home/grand/web/grandgold.jewelry/public_html/bitrix/backup/{filename.replace("grandgold.jewelry_", "")}')
