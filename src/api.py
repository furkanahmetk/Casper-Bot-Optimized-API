from flask import Blueprint
from src.model import validator, metrics
from flask_apispec import use_kwargs, marshal_with
from marshmallow import Schema
from webargs import fields

api = Blueprint('api', __name__)


validator = validator.Validator()
metrics = metrics.Metrics()


class ApiResponse(Schema):
    message = fields.Str()


class ValidatorResponse(Schema):
    public_key = fields.Str()
    is_active = fields.Bool()
    fee = fields.Float()
    total_stake = fields.Str()
    delegators_number = fields.Int()
    performance =fields.Float()

# Endpoint for returning state of validator's from given public key


@api.route('/state', methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getState(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    if validator_object["is_active"]:
        return {"message": f"{pubKey}: active"}
    else:
        return {"message": f"{pubKey}: not active"}

# Endpoint for returning delegation fee of validator's from given public key


@api.route('/delegationRate', methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getDelegationRate(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey}'s delegation fee: {validator_object['fee']}%"}

# Endpoint for returning total stake of validator's from given public key


@api.route('/totalStake', methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getTotalStake(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey}'s total stake: {validator_object['total_stake']} "}

# Endpoint for returning delegator number of validator's from given public key


@api.route('/totalDelegators', methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getTotalDelegators(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey}'s delegator number: {validator_object['delegators_number']}"}

# Endpoint for returning performance of validator's from given public key


@api.route('/performance', methods=['GET'])
@use_kwargs({'pubKey': fields.Str()}, location='querystring')
@marshal_with(ApiResponse())
def getPerformance(pubKey):
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey}'s performance: {validator_object['performance']}"}


# Endpoint for returning all validators from given public keys
@api.route('/getAllValidatorValues', methods=['POST'])
@use_kwargs({'publicKeys': fields.List(fields.Str())})
@marshal_with(ValidatorResponse(many=True))
def getAllValidatorValues(publicKeys):
    validator_object = validator.find({"public_key": {"$in": publicKeys}})
    validator_list = []
    for item in validator_object:
        validator_list.append(
            {
                'public_key': item['public_key'],
                'is_active': item['is_active'],
                'fee': item['fee'],
                'total_stake': item['total_stake'],
                'delegators_number': item['delegators_number'],
                'performance': item['performance']

            }
        )
    return validator_list

# Endpoint for latest apy


@api.route('/apy', methods=['GET'])
@marshal_with(ApiResponse())
def getApy():
    current_metrics = metrics.find({})
    apy = current_metrics[0]['apy']
    return {"message": f"apy: {float('{:.2f}'.format(apy))}%"}


# Endpoint for latest uptime
@api.route('/uptime', methods=['GET'])
@marshal_with(ApiResponse())
def getUptime():
    current_metrics = metrics.find({})
    uptime = current_metrics[0]['uptime']
    return {"message": f"uptime: {uptime}%"}
