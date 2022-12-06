"""
Author: Lucas Henrique Messias Gonçalves
Date: september 29th 2022
Function of this code: This Script sends messages to slack, whom is communicate through an API.
Support Links: https://api.slack.com/web, https://slack.com/intl/pt-br/
https://www.youtube.com/watch?v=6gHvqXrfjuo&list=PLzMcBGfZo4-kqyzTzJWCV6lyK-ZMYECDc&index=2
"""

import slack
import os
from pathlib import Path
from dotenv import load_dotenv

message = "Aqui vai a menssagem que será enviada"
channel_token='#general'
env_path = Path('.') / '.env'
load_dotenv = slack.WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel='{}'.format(channel_token), text="{}".format(message))