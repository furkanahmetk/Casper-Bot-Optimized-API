
from src.model import validator
import uuid



    
def test_key(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/state' endpoint is posted to 
    THEN check the response is valid
    """
    public_key = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "era_id": 1907,
        "public_key": public_key,
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

    response = get(f'/state?pubKey={public_key}')

    assert public_key.encode() in response.data 


def test_status_code(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/state' endpoint is posted to 
    THEN check the response is valid
    """
    public_key = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "era_id": 1907,
        "public_key": public_key,
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

    response = get(f'/state?pubKey={public_key}')

    assert not response.status_code != 200


def test_data(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/state' endpoint is posted to 
    THEN check the response is valid
    """
    public_key = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "era_id": 1907,
        "public_key": public_key,
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

    response = get(f'/state?pubKey={public_key}')

    assert b'not active' in response.data 