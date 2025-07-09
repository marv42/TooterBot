#!/usr/bin/env python3
import logging
import requests
from subprocess import Popen, PIPE

from mastodon import Mastodon, MastodonIllegalArgumentError


class TooterBot:
    def __init__(self, client_secret_file):
        self.client_secret_file = client_secret_file

    def get_client_id(self):
        with open(self.client_secret_file) as f:
            return f.readlines()[0].strip()

    def get_client_secret(self):
        with open(self.client_secret_file) as f:
            return f.readlines()[1].strip()

    def get_url(self):
        with open(self.client_secret_file) as f:
            return f.readlines()[2].strip()

    def register(self, client_name):
        Mastodon.create_app(
            client_name,
            api_base_url='https://mas.to',
            to_file=self.client_secret_file)

    def print_version(self):
        mastodon = Mastodon(client_id=self.client_secret_file)
        version = mastodon.retrieve_mastodon_version()
        logging.debug(f"Mastodon version {version}")

    def get_access_token(self):
        response = requests.post(
            f'{self.get_url()}/oauth/token',
            data={'grant_type': 'client_credentials',
                  'client_id': self.get_client_id(),
                  'client_secret': self.get_client_secret(),
                  'scope': 'read write follow'})
         return response.json()['access_token']

    def get_instance(self, access_token):
        return Mastodon(client_id=self.client_secret_file, access_token=access_token)

    def toot(self, access_token, text):
        mastodon = self.get_instance(access_token)
        mastodon.toot(text)

    def login_and_toot(self, access_token, text):
        logging.basicConfig(level=logging.DEBUG)
        try:
            self.print_version()
            # access_token = self.get_access_token()
            self.toot(access_token, text)
            # self.get_instance(access_token).revoke_access_token()
        except MastodonIllegalArgumentError as e:
            Popen(["mail", "-s", "Failed to login", "marv42@gmail.com"], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(str(e.args).encode())
