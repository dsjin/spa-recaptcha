import os
import json
import requests

RECAPTCHA_URL = 'https://www.google.com/recaptcha/api/siteverify'

class RecaptchaVerifyError(Exception):
    pass

class UnknownError(Exception):
    pass

def lambda_handler(event, context):
    recaptcha_data = {
        'secret': os.environ.get('RECAPTCHA_SECRET'),
        'response': event['recaptcha_token']
    }
    recaptcha_res = requests.post(RECAPTCHA_URL, recaptcha_data)
    recaptcha_data = recaptcha_res.json()
    res = {
        'body': {
            'recaptcha_verified': recaptcha_data
        }
    }
    if (recaptcha_data['success']):
        res['body'].update(
            event
        )
        return res
    else:
        raise RecaptchaVerifyError(json.dumps({
            'StatusCode': 401,
            **res
        }))
