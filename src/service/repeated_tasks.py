from src.service import data
from src.model import validator
from src.model import metrics
"""
Defines repeated jobs of the system. It calls, controls and saves the data flow to the system. It seperates the data already in the system with the new data.
It either inserts or updates the data
"""


class Repeated_Task():

    def __init__(self):
        self.data = data.Data()
        self.validator = validator.Validator()
        self.metrics = metrics.Metrics()

    def data_cron(self):
        # Get validator data from data object
        validator_list = self.data.get_validator_list()

        # Create public key list and dictionary of object from current validators to compare
        current_validator_public_keys = [
            item['public_key'] for item in validator_list]
        current_validator_dict = {
            item['public_key']: item for item in validator_list}

        # Find which of the current validators have entry in the database and create public key list and dictionary of object out of them
        validators_in_db = self.validator.find(
            {"public_key": {"$in": current_validator_public_keys}})
        validators_in_db_public_keys = [
            item['public_key'] for item in validators_in_db]
        validators_in_db_dict = {item['public_key']
            : item for item in validators_in_db}

        # Find which of the objects should be updated
        update_validators = list(set(validators_in_db_public_keys).intersection(
            set(current_validator_public_keys)))
        # Find which validators are new and an entry should created in the database
        insert_validators = list(
            set(current_validator_public_keys)-set(validators_in_db_public_keys))

        if len(insert_validators) > 0:
            self.validator.create_many(
                [{
                    'public_key': current_validator_dict[x]['public_key'],
                    'is_active': current_validator_dict[x]['is_active'],
                    'fee': current_validator_dict[x]['fee'],
                    'delegators_number': current_validator_dict[x]['delegators_number'],
                    'self_stake': current_validator_dict[x]['self_stake'],
                    'total_stake': current_validator_dict[x]['total_stake'],
                    'delegator_stake': current_validator_dict[x]['delegator_stake'],
                    'self_share': current_validator_dict[x]['self_share'],
                    'network_share': current_validator_dict[x]['network_share'],
                    'rank': current_validator_dict[x]['rank'],
                    'era_id': current_validator_dict[x]['era_id'],
                    'bid_amount': current_validator_dict[x]['bid_amount'],
                    'performance': current_validator_dict[x]['average_performance']['average_score']
                } for x in insert_validators])
        if len(update_validators) > 0:
            new_validator_list = []
            for v_pub_key in update_validators:
                id = validators_in_db_dict[v_pub_key]['_id']
                item = {
                    '_id':id,   
                    'public_key': current_validator_dict[v_pub_key]['public_key'],
                    'is_active': current_validator_dict[v_pub_key]['is_active'],
                    'fee': current_validator_dict[v_pub_key]['fee'],
                    'delegators_number': current_validator_dict[v_pub_key]['delegators_number'],
                    'self_stake': current_validator_dict[v_pub_key]['self_stake'],
                    'total_stake': current_validator_dict[v_pub_key]['total_stake'],
                    'delegator_stake': current_validator_dict[v_pub_key]['delegator_stake'],
                    'self_share': current_validator_dict[v_pub_key]['self_share'],
                    'network_share': current_validator_dict[v_pub_key]['network_share'],
                    'rank': current_validator_dict[v_pub_key]['rank'],
                    'era_id': current_validator_dict[v_pub_key]['era_id'],
                    'bid_amount': current_validator_dict[v_pub_key]['bid_amount'],
                    'performance': current_validator_dict[v_pub_key]['average_performance']['average_score'],
                    'created': validators_in_db_dict[v_pub_key]['created'],
                    'updated': validators_in_db_dict[v_pub_key]['updated']
                }  
                new_validator_list.append(item)
            self.validator.update_many(new_validator_list)

    def metrics_cron(self):
        uptime, total_supply, era_stake = self.data.get_metrics()
        total_supply = float(total_supply)
        era_stake = float(era_stake)
        old_metric = self.metrics.find({})

        if len(old_metric) == 0:
            self.metrics.create({
                "uptime": uptime,
                "apy": total_supply*.08*100000000000/era_stake,
                "total_suply": total_supply,
                "era_stake": era_stake,
            })
        else:
            self.metrics.update(old_metric[0]["_id"],{
                "uptime": uptime,
                "apy": total_supply*.08*100000000000/era_stake,
                "total_suply": total_supply,
                "era_stake": era_stake,
            })
