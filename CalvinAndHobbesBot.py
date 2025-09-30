#!/usr/bin/env python3
import argparse
from datetime import date, timedelta
from random import randrange

from calvin_and_hobbes_credentials import access_token
from TooterBot import TooterBot

CLIENT_NAME = 'pytooterappcalvinandhobbes'
CLIENT_SECRET_FILE = 'pytooter_clientcred_calvinandhobbes.secret'
DATE_OF_THE_FIRST_COMIC = '1985-11-18'


def parse_args():
    parser = argparse.ArgumentParser(description='toot daily')
    parser.add_argument('--random', action='store_true', help='toot randomly')
    return parser.parse_args()


calvin_and_hobbes_bot = TooterBot(CLIENT_SECRET_FILE)
# calvin_and_hobbes_bot.register(CLIENT_NAME); sys.exit()  # this only needs to be done once

comic_date = date.today()
text = "daily"

if parse_args().random:
    first_date = date.fromisoformat(DATE_OF_THE_FIRST_COMIC)
    date_delta = comic_date - first_date
    random_number_of_days = randrange(date_delta.days)
    comic_date = first_date + timedelta(days=random_number_of_days)
    text = "random"

text = f"{text} #CalvinAndHobbes comic:\n" \
       f"https://www.gocomics.com/calvinandhobbes/{comic_date.year}/{comic_date.month:02d}/{comic_date.day:02d}"
calvin_and_hobbes_bot.toot(access_token, text)
