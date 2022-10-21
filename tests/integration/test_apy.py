from src.model import metrics


def test_size(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/apy' endpoint is posted to 
    THEN check the response is valid
    """
    metric_object = metrics.Metrics()
    current_metrics = metric_object.find({})
    if len(current_metrics) == 0:
        metric_object.create({
            "uptime": "1month 26days 4h 12m 3s 652ms",
            "apy": 10.442945446577596,
            "total_suply": 11230232456,
            "era_stake": 8603114907340900000,
        })
    else:
        metric_object.delete(current_metrics[0]["_id"])
        metric_object.create({
            "uptime": "1month 26days 4h 12m 3s 652ms",
            "apy": 10.442945446577596,
            "total_suply": 11230232456,
            "era_stake": 8603114907340900000,
        })
    response = get('/apy')

    assert b"10.44" in response.data 

def test_status_code(get):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/apy' endpoint is posted to 
    THEN check the response is valid
    """
    metric_object = metrics.Metrics()
    current_metrics = metric_object.find({})
    if len(current_metrics) == 0:
        metric_object.create({
            "uptime": "1month 26days 4h 12m 3s 652ms",
            "apy": 10.442945446577596,
            "total_suply": 11230232456,
            "era_stake": 8603114907340900000,
        })
    else:
        metric_object.delete(current_metrics[0]["_id"])
        metric_object.create({
            "uptime": "1month 26days 4h 12m 3s 652ms",
            "apy": 10.442945446577596,
            "total_suply": 11230232456,
            "era_stake": 8603114907340900000,
        })
    response = get('/apy')
    
    assert not response.status_code != 200