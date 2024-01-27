#!/usr/bin/env python3
from subprocess import Popen, PIPE

from credentials import username, password, clientId, clientSecret
from mastodon import Mastodon, MastodonIllegalArgumentError
from datetime import date


def register():
    Mastodon.create_app(
        clientName,
        api_base_url=apiBaseUrl,
        to_file=clientCredentialsFile)
        # user_agent='Mozilla 5.0')


def login():
    mastodon = Mastodon(
        client_id=clientId,  # TODO client_id=clientCredentialsFile,
        client_secret=clientSecret,
        api_base_url=apiBaseUrl)
    version = mastodon.retrieve_mastodon_version()
    mastodon.log_in(username, password, to_file=userCredentialsFile)


def get_instance():
    return Mastodon(
        access_token=userCredentialsFile,
        api_base_url=apiBaseUrl)


def toot_daily():
    mastodon = get_instance()
    today = date.today()
    mastodon.toot(f"""Was geschah heute #vor100Jahren?
https://chroniknet.de/extra/was-war-am/?ereignisdatum={today.day}.{today.month}.{today.year - 100}""")


clientName = 'pytooterappwasgeschah'
apiBaseUrl = 'https://botsin.space'
clientCredentialsFile = 'pytooter_clientcred_wasgeschah.secret'
userCredentialsFile = 'pytooter_usercred_wasgeschah.secret'


if __name__ == '__main__':
    # register()  # this only needs to be done once
    try:
        login()
    except MastodonIllegalArgumentError as e:
        Popen(["mail", "-s", "Failed to login", "marv42+wasgeschah@gmail.com"], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(str(e.args).encode())
    toot_daily()
    get_instance().revoke_access_token()
