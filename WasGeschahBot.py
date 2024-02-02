#!/usr/bin/env python3
import logging
import re
import sys
from subprocess import Popen, PIPE

from credentials import username, password, client_id, client_secret
from mastodon import Mastodon, MastodonIllegalArgumentError
from datetime import date


API_BASE_URL = 'https://botsin.space'


def register():
    client_credentials_file = 'pytooter_clientcred_wasgeschah.secret'
    client_id, client_secret = Mastodon.create_app(
        'pytooterappwasgeschah',
        api_base_url=API_BASE_URL)
        # to_file=client_credentials_file)
        # user_agent='Mozilla/5.0')
    write_client_credentials(client_id, client_secret)


def write_client_credentials(id, secret):
    with open("credentials.py", "r+") as f:
        content = f.read()
        f.seek(0)
        content = re.sub('client_id.*', f"client_id = '{id}'", content)
        content = re.sub('client_secret.*', f"client_secret = '{secret}'", content)
        f.write(content)
        f.truncate()


def login():
    mastodon = Mastodon(
        client_id=client_id,
        client_secret=client_secret,
        api_base_url=API_BASE_URL)
    version = mastodon.retrieve_mastodon_version()
    logging.debug(f"Mastodon version {version}")
    return mastodon.log_in(username, password)  # , to_file=userCredentialsFile)


def get_instance(token):
    return Mastodon(
        client_id=client_id,
        client_secret=client_secret,
        access_token=token,
        api_base_url=API_BASE_URL)


def toot_daily(token):
    mastodon = get_instance(token)
    today = date.today()
    mastodon.toot(f"""Was geschah heute #vor100Jahren?
https://chroniknet.de/extra/was-war-am/?ereignisdatum={today.day}.{today.month}.{today.year - 100}""")


if __name__ == '__main__':
    # register(); sys.exit()  # this only needs to be done once
    try:
        access_token = login()
        toot_daily(access_token)
        get_instance(access_token).revoke_access_token()
    except MastodonIllegalArgumentError as e:
        Popen(["mail", "-s", "Failed to login", username], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(str(e.args).encode())
