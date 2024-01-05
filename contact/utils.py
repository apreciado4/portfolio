from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, PlainTextContent, HtmlContent, ReplyTo
import os
from django.http import Http404


def send_email(reply_to, subject, content):
    message = Mail(
        from_email='email@apreciado4.com',
        to_emails='apreciado4@live.com',
        subject=subject,
        plain_text_content=PlainTextContent(content),
        # html_content=HtmlContent(content),
    )
    message.reply_to = reply_to
    try:
        sendgrid_client = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message=message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        return response.status_code
    except Exception as e:
        raise Http404
