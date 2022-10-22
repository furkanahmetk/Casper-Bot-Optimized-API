from src.factory.validation import Validation
from src.factory.database import Database
from src.errors import APIError


class Metrics(object):
    def __init__(self):
        self.validator = Validation()
        self.collection_name = 'metrics'
        

        self.fields = {
            "_id":"string",
            "uptime": "string",
            "apy": "float",
            "total_suply": "float",
            "era_stake": "float",
            "created": "datetime",
            "updated": "datetime",
        }

        self.create_required_fields = ["uptime", "apy","total_suply","era_stake"]

        # Fields optional for CREATE
        self.create_optional_fields = ["_id","created","updated"]

        # Fields required for UPDATE
        self.update_required_fields = ["uptime", "apy","total_suply","era_stake"]
        # Fields optional for UPDATE
        self.update_optional_fields = ["_id","created","updated"]

    def create(self, validator):
        # Validator will throw error if invalid
        self.validator.validate(
            validator, self.fields, self.create_required_fields, self.create_optional_fields)
        res = Database.insert(validator, self.collection_name)
        return "Inserted Id " + res

    def find(self, validator):  # find all
        return Database.find(validator, self.collection_name)

    def update(self, id, validator):
        self.validator.validate(
            validator, self.fields, self.update_required_fields, self.update_optional_fields)
        return Database.update(id, validator, self.collection_name)

    def delete(self, id):
        return Database.delete(id, self.collection_name)
