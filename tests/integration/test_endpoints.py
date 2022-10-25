
from src.model import validator
import uuid


def test_total_stake(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/totalStake' endpoint is posted to 
    THEN check the response is valid
    """
    validate = validator.Validator()
    public_key = str(uuid.uuid4())
    validate.create({
        "era_id": 1907,
        "public_key": public_key,
        "is_active": True,
        "fee": 25,
        "delegators_number": 42,
        "self_stake": "1207026548335",
        "total_stake": "1915602215052068",
        "delegator_stake": "1914395188503733",
        "self_share": "0.06",
        "network_share": "0.02",
        "rank": 83,
        "performance":99.5
    })
    response = get(f'/totalStake?pubKey={public_key}')

    assert public_key.encode() in response.data 
    assert not response.status_code != 200
    assert b'1915602215052068' in response.data 


def test_delegationRate(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/delegationRate' endpoint is posted to 
    THEN check the response is valid
    """
    public_key = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "era_id": 1907,
        "public_key": public_key,
        "is_active": True,
        "fee": 25,
        "delegators_number": 42,
        "self_stake": "1207026548335",
        "total_stake": "1915602215052068",
        "delegator_stake": "1914395188503733",
        "self_share": "0.06",
        "network_share": "0.02",
        "rank": 83,
        "performance":99.5
    })

    response = get(f'/delegationRate?pubKey={public_key}')

    assert public_key.encode() in response.data 
    assert not response.status_code != 200
    assert b'25' in response.data 

    
def test_state(get):
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
        "rank": 83,
        "performance":99.5
    })

    response = get(f'/state?pubKey={public_key}')

    assert public_key.encode() in response.data 
    assert not response.status_code != 200
    assert b'not active' in response.data 

def test_totalDelegators(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/totalDelegators' endpoint is posted to 
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
        "rank": 83,
        "performance":99.5
    })

    response = get(f'/totalDelegators?pubKey={public_key}')

    assert public_key.encode() in response.data 
    assert not response.status_code != 200
    assert b'42' in response.data 