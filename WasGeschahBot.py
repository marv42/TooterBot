#!/usr/bin/env python3
from datetime import date

from was_geschah_credentials import access_token
from TooterBot import TooterBot


CLIENT_NAME = 'pytooterapp_wasgeschah'
CLIENT_SECRET_FILE = 'pytooter_clientcred_wasgeschah.secret'

was_geschah_bot = TooterBot(CLIENT_SECRET_FILE)
# was_geschah_bot.register(CLIENT_NAME); sys.exit()  # this only needs to be done once

today = date.today()
text = f"""Was geschah heute #vor100Jahren?
https://chroniknet.de/was-war-am/{today.day}.{today.month}.{today.year - 100}"""
was_geschah_bot.toot(access_token, text)
