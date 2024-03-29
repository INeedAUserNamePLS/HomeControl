from __future__ import print_function
import base64
from email.mime.text import MIMEText

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from requests import HTTPError
from jinja2 import Template

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def getService():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Call the Gmail API
    return build("gmail", "v1", credentials=creds)


def sendTwoFactor(receiverMail, code, host):
    service = getService()
    #
    with open(os.getcwd() + "/lights/templates/mails/twoFactor.html", "r") as f:
        template = Template(f.read())
    html = template.render(code=code, host=host)
    html_message = MIMEText(html, "html")
    html_message["from"] = "HomeControl <home.controller.hc@gmail.com>"
    html_message["to"] = receiverMail
    html_message["subject"] = "Activation HomeControl-Account"

    create_message = {"raw": base64.urlsafe_b64encode(html_message.as_bytes()).decode()}
    try:
        message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None


def sendReset(receiverMail, userid, code, host):
    service = getService()
    #
    with open(os.getcwd() + "/lights/templates/mails/resetPassword.html", "r") as f:
        template = Template(f.read())
    html = template.render(userid=userid, code=code, host=host)
    html_message = MIMEText(html, "html")
    html_message["from"] = "HomeControl <home.controller.hc@gmail.com>"
    html_message["to"] = receiverMail
    html_message["subject"] = "Password Recovery HomeControl-Account"

    create_message = {"raw": base64.urlsafe_b64encode(html_message.as_bytes()).decode()}
    try:
        message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None
