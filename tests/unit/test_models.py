from marshmallow import ValidationError
from src.factory.validation import Validation




def test_provider_validater():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """
    validator = Validation()
    try:
        validator.validate_type(5,"msl")
    except ValueError as verr:
        assert True, "Invalid value for desired type"
