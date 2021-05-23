from credentials import username, password, clientId, clientSecret
from mastodon import Mastodon
from datetime import date, timedelta


def register():
    Mastodon.create_app(
        clientName,
        api_base_url=apiBaseUrl,
        to_file=clientCredentialsFile)


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
    # TODO Check if site exists
    mastodon.toot(f"""Was geschah heute vor 100 Jahren?
https://chroniknet.de/extra/was-war-am/?ereignisdatum={today.day}.{today.month}.{today.year - 100}""")


clientName = 'pytooterappwasgeschah'
apiBaseUrl = 'https://botsin.space'
clientCredentialsFile = 'pytooter_clientcred_wasgeschah.secret'
userCredentialsFile = 'pytooter_usercred_wasgeschah.secret'


if __name__ == '__main__':
    # register()  # this only needs to be done once
    login()
    toot_daily()
