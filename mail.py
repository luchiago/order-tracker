import os
import requests
import logging

def send_mail(email: str, date: str, status: str):
    MAILGUN_URL = os.getenv('MAILGUN_URL')
    MAILGUN_DOMAIN_NAME = os.getenv('MAILGUN_DOMAIN_NAME')
    MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
    EMAIL_FROM_USER_NAME = os.getenv('EMAIL_FROM_USER_NAME')
    EMAIL_FROM_USER_EMAIL = os.getenv('EMAIL_FROM_USER_EMAIL')

    url = f'{MAILGUN_URL}{MAILGUN_DOMAIN_NAME}/messages'

    logging.info('Sending email')

    result = requests.post(url,
            auth=('api', MAILGUN_API_KEY),
            data={'from': f'{EMAIL_FROM_USER_NAME} <{EMAIL_FROM_USER_EMAIL}>',
                'to': [email],
                'subject': 'UPDATE ON STATUS',
                'text': f'{date} {status}'
            }
        )

    logging.info(f'Send email status code: {result.status_code}')
