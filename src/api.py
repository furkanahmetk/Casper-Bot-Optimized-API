from flask import Blueprint
from src.model import validator
from flask_apispec import use_kwargs, marshal_with
from marshmallow import Schema
from webargs import fields

api = Blueprint('api', __name__)


validator = validator.Validator()
class ApiResponse(Schema):
     message = fields.Str()

#Endpoint for returning state of validator's from given public key
@api.route('/state',methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getState(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    if validator_object["is_active"]:
        return {"message": f"{pubKey} is Active"}
    else:
        return {"message": f"{pubKey} is not Active"}

#Endpoint for returning delegation fee of validator's from given public key   
@api.route('/delegationRate',methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getDelegationRate(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey} {validator_object['fee']}% delegation fees"}

#Endpoint for returning total stake of validator's from given public key   
@api.route('/totalStake',methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getTotalStake(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey} has {validator_object['total_stake']} total stake"}

#Endpoint for returning delegator number of validator's from given public key   
@api.route('/totalDelegators',methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getTotalDelegators(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey} has {validator_object['delegators_number']} delegators"}




