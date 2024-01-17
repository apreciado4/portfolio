from django.conf import settings
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail, From, To, PlainTextContent, HtmlContent, ReplyTo
import os
from django.core.mail import send_mail
from django.http import Http404

FROM_ADDRESS = 'DoNotReply@e65ef710-8fc7-4ebe-b2ff-65a4837a6dfe.azurecomm.net'
SEND_ADDRESS = 'apreciado4@live.com'


def send_email(reply_to, subject, content):
    try:
        response = send_mail(
            subject,
            content,
            FROM_ADDRESS,
            [SEND_ADDRESS],
            fail_silently=False,
        )
        return response
    except Exception as e:
        raise Http404
