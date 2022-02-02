import logging

import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    r = requests.get('http://www.icanhazip.com')
    logging.info(r)
    return func.HttpResponse(
            "{}".format(r.text),
            status_code=200
    )
