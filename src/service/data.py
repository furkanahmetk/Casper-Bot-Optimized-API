import requests

from src.config import Config

"""
Onject that speciliazed for daflow to the system. It retrieves data from given address.
"""
class Data(object):

    def __init__(self):
        self.base_url= Config.BASE_URL
    
    def get_validator_list(self):
        current_era = self.get_current_era()
        page = 1
        validators = []
        PARAMS = {'era_id':current_era,'page':page}
        r = requests.get(url = self.base_url+'/validators', params = PARAMS)
        data = r.json()
        validators.extend(data['data'])
        while data['pageCount']>page:
            page += 1
            PARAMS = {'era_id':current_era,'page':page}
            r = requests.get(url = self.base_url+'/validators', params = PARAMS)
            data = r.json()
            validators.extend(data['data'])
        return validators


    def get_current_era(self):
        r = requests.get(url = self.base_url+'/rpc/info_get_status', params = {})
        data = r.json()
        current_era = data['result']['last_added_block_info']['era_id']
        return current_era

    def get_metrics(self):
        r = requests.get(url = self.base_url+'/rpc/info_get_status', params = {})
        data = r.json()
        uptime = data['result']['uptime']
        r = requests.get(url = self.base_url+'/supply', params = {})
        data = r.json()
        total_supply = data['data']['total']
        r = requests.get(url = self.base_url+'/auction-metrics', params = {})
        data = r.json()
        era_stake = data['total_active_era_stake']

        return uptime,total_supply,era_stake