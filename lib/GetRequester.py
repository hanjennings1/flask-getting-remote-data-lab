import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # send a GET request to the stored URL
        response = requests.get(self.url)
        # return the raw response body as bytes
        return response.content

    def load_json(self):
        # reuse get_response_body to fetch the raw bytes
        body = self.get_response_body()
        # parse the JSON bytes into a Python list/dict
        return json.loads(body)
    