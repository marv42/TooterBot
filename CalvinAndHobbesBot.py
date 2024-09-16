#!/usr/bin/env python3
import argparse
import sys
import urllib.request
from datetime import date

from calvin_and_hobbes_credentials import username, password
from TooterBot import TooterBot

CLIENT_NAME = 'pytooterappcalvinandhobbes'
CLIENT_SECRET_FILE = 'pytooter_clientcred_calvinandhobbes.secret'


def parse_args():
    parser = argparse.ArgumentParser(description='toot daily')
    parser.add_argument('--random', action='store_true', help='toot randomly')
    return parser.parse_args()


calvin_and_hobbes_bot = TooterBot(CLIENT_SECRET_FILE)
# calvin_and_hobbes_bot.register(CLIENT_NAME); sys.exit()  # this only needs to be done once

url = urllib.request.urlopen('https://www.gocomics.com/random/calvinandhobbes').geturl()
text = f"random #CalvinAndHobbes comic:\n{url}"
if not parse_args().random:
    today = date.today()
    # yesterday = today - timedelta(days=1)  # because of time zone differences
    text = f"daily #CalvinAndHobbes comic:\nhttps://www.gocomics.com/calvinandhobbes/{today.year}/{today.month:02d}/{today.day:02d}"
calvin_and_hobbes_bot.login_and_toot(username, password, text)
