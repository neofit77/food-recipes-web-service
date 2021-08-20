import os
import requests
import clearbit

clearbit.key = os.environ.get('clearbit_key')
hunter_key = os.environ.get('hunter_key')

def verified(email):
    api_key = hunter_key

    status = requests.get('https://api.hunter.io/v2/email-verifier?email={}&api_key={}'.format(email, api_key)).json()
    return status['data']['status']


def additional_data(email):
    res = clearbit.Enrichment.find(email='alex@clearbit.com', stream=True)
    return res