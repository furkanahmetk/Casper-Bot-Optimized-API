from src.model import validator
import uuid
import json

def test_size(post):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/getAllValidatorValues' endpoint is posted to 
    THEN check the response is valid
    """
    public_key_1 = str(uuid.uuid4())
    public_key_2 = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "era_id": 1907,
        "public_key": public_key_1,
        "is_active": False,
        "fee": 25,
        "delegators_number": 42,
        "self_stake": "1207026548335",
        "total_stake": "1915602215052068",
        "delegator_stake": "1914395188503733",
        "self_share": "0.06",
        "network_share": "0.02",
        "rank": 83
    })

    validate.create({
        "era_id": 1908,
        "public_key": public_key_2,
        "is_active": False,
        "fee": 25,
        "delegators_number": 42,
        "self_stake": "1207026548335",
        "total_stake": "1915602215052068",
        "delegator_stake": "1914395188503733",
        "self_share": "0.06",
        "network_share": "0.02",
        "rank": 2
    })
    response = post('/getAllValidatorValues',data=dict(publicKeys=[public_key_1,public_key_2]))
    response_data =  json.loads(response.data.decode('utf-8'))

    assert len(response_data)  == 2


def test_status_code(post):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/getAllValidatorValues' endpoint is posted to 
    THEN check the response is valid
    """
    public_key_1 = str(uuid.uuid4())
    public_key_2 = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "era_id": 1907,
        "public_key": public_key_1,
        "is_active": False,
        "fee": 25,
        "delegators_number": 42,
        "self_stake": "1207026548335",
        "total_stake": "1915602215052068",
        "delegator_stake": "1914395188503733",
        "self_share": "0.06",
        "network_share": "0.02",
        "rank": 83
    })

    validate.create({
        "era_id": 1908,
        "public_key": public_key_2,
        "is_active": False,
        "fee": 25,
        "delegators_number": 42,
        "self_stake": "1207026548335",
        "total_stake": "1915602215052068",
        "delegator_stake": "1914395188503733",
        "self_share": "0.06",
        "network_share": "0.02",
        "rank": 2
    })
    response = post('/getAllValidatorValues',data=dict(publicKeys=[public_key_1,public_key_2]))
    
    assert not response.status_code != 200