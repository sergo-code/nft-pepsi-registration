import os.path
import base64
from bs4 import BeautifulSoup
from lxml import etree
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']


def read_email():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('creds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = results.get('messages', [])
    if not messages:
        return False
    else:
        message_count = 0
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            email_data = msg['payload']['headers']
            for values in email_data:
                name = values['name']
                if name == 'From':
                    from_name = values['value']
                    if from_name == 'MicDrop <noreply@themicdrop.pepsi.com>':

                        data = msg['payload']['body']["data"]
                        byte_code = base64.urlsafe_b64decode(data)

                        text = byte_code.decode("utf-8")
                        soup = BeautifulSoup(text, "lxml")
                        dom = etree.HTML(str(soup))
                        link = dom.xpath("//a[text()='Activate Account']/@href")[0]
                    else:
                        link = False
                    service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()
                    return link


if __name__ == '__main__':
    link = read_email()

    print(link)
