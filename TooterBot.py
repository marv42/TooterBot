#!/usr/bin/env python3
import logging
import requests
from subprocess import Popen, PIPE

from mastodon import Mastodon, MastodonIllegalArgumentError


class TooterBot:
    def __init__(self, client_secret_file):
        self.client_secret_file = client_secret_file

    def register(self, client_name):
        Mastodon.create_app(
            client_name,
            api_base_url='https://mas.to',
            to_file=self.client_secret_file)

    def get_instance(self, access_token=None):
        if access_token is None:
            return Mastodon(client_id=self.client_secret_file)
        return Mastodon(client_id=self.client_secret_file, access_token=access_token)

    def toot(self, access_token, text):
        logging.basicConfig(level=logging.DEBUG)
        try:
            mastodon = self.get_instance(access_token)
            logging.debug(f"Mastodon version {mastodon.retrieve_mastodon_version()}")
            mastodon.toot(text)  # status_post
        except MastodonIllegalArgumentError as e:
            Popen(["mail", "-s", "Failed to login", "marv42@gmail.com"], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(str(e.args).encode())
