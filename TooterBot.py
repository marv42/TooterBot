#!/usr/bin/env python3
import logging
from subprocess import Popen, PIPE

from mastodon import Mastodon, MastodonIllegalArgumentError

API_BASE_URL = 'https://botsin.space'


class TooterBot:
    def __init__(self, client_secret_file):
        self.client_secret_file = client_secret_file

    def register(self, client_name):
        Mastodon.create_app(
            client_name,
            api_base_url=API_BASE_URL,
            to_file=self.client_secret_file)

    def login(self, username, password):
        mastodon = Mastodon(client_id=self.client_secret_file, api_base_url=API_BASE_URL)
        version = mastodon.retrieve_mastodon_version()
        logging.debug(f"Mastodon version {version}")
        return mastodon.log_in(username, password)  # , to_file=userCredentialsFile)

    def get_instance(self, token):
        return Mastodon(client_id=self.client_secret_file, api_base_url=API_BASE_URL, access_token=token)

    def toot(self, token, text):
        mastodon = self.get_instance(token)
        mastodon.toot(text)

    def login_and_toot(self, username, password, text):
        logging.basicConfig(level=logging.DEBUG)
        try:
            access_token = self.login(username, password)
            logging.debug(f"access_token: {access_token}")
            self.toot(access_token, text)
            self.get_instance(access_token).revoke_access_token()
        except MastodonIllegalArgumentError as e:
            Popen(["mail", "-s", "Failed to login", username], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(str(e.args).encode())
