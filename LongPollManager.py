import requests
import json
__author__ = 'deffe'


class LongPollManager:
    def __init__(self, lp_data):
        self.server = lp_data[u'server']
        self.key = lp_data[u'key']
        self.ts = lp_data[u'ts']
        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/json'
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'

    def get_url(self):
        url = "http://{server}?act=a_check&key={key}&ts={ts}&wait={timeout}&mode=2".format(
            server=self.server,
            key=self.key,
            ts=self.ts,
            timeout=25,
        )
        return url

    def connect(self):
        response = self.session.get(self.get_url())
        data = json.loads(response.text)
        self.ts = data['ts']
        return data['updates']
