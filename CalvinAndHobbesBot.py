#!/usr/bin/env python3
import argparse
import re
import requests
from datetime import date, timedelta
from random import randrange

from calvin_and_hobbes_credentials import access_token
from TooterBot import TooterBot

CLIENT_NAME = 'pytooterappcalvinandhobbes'
CLIENT_SECRET_FILE = 'pytooter_clientcred_calvinandhobbes.secret'
CALVIN_AND_HOBBES_BASE_URL = 'https://www.gocomics.com/calvinandhobbes/'
DATE_OF_THE_FIRST_COMIC = '1985-11-18'


def parse_args():
    parser = argparse.ArgumentParser(description='toot daily')
    parser.add_argument('--random', action='store_true', help='toot randomly')
    return parser.parse_args()

def get_comic_site_url(date):
    return f"{CALVIN_AND_HOBBES_BASE_URL}{date.year}/{date.month:02d}/{date.day:02d}"

calvin_and_hobbes_bot = TooterBot(CLIENT_SECRET_FILE)
# calvin_and_hobbes_bot.register(CLIENT_NAME); sys.exit()  # this only needs to be done once

comic_date = date.today()
url = get_comic_site_url(comic_date)
text = "daily"

if parse_args().random:
    first_date = date.fromisoformat(DATE_OF_THE_FIRST_COMIC)
    date_delta = comic_date - first_date
    random_number_of_days = randrange(date_delta.days)
    comic_date = first_date + timedelta(days=random_number_of_days)
    url = get_comic_site_url(comic_date)
    result = requests.get(url)
    if not result.ok:
        raise Exception("Error getting web site")
    m = re.search('(https://featureassets.gocomics.com/assets/.*?)"', result.text)
    url = m.group(1)
    text = "random"

text = f"{text} #CalvinAndHobbes comic:\n{url}"
calvin_and_hobbes_bot.toot(access_token, text)
