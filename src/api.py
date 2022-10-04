from crypt import methods
from flask import Blueprint, jsonify,request
from src.model import validator
api = Blueprint('api', __name__)


validator = validator.Validator()

#Endpoint for returning state of validator's from given public key
@api.route('/state',methods=['GET'])
def getState():
    pubKey = request.args.get('pubKey', default = 1, type = str)
    validator_object = validator.find_one_by_public_key(pubKey)
    if validator_object["is_active"]:
        return {"message": f"{pubKey} is Active"}
    else:
        return {"message": f"{pubKey} is not Active"}

#Endpoint for returning delegation fee of validator's from given public key   
@api.route('/delegationRate',methods=['GET'])
def getDelegationRate():
    pubKey = request.args.get('pubKey', default = 1, type = str)
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey} {validator_object['fee']}% delegation fees"}
#Endpoint for returning total stake of validator's from given public key   
@api.route('/totalStake',methods=['GET'])
def getTotalStake():
    pubKey = request.args.get('pubKey', default = 1, type = str)
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey} has {validator_object['total_stake']} total stake"}

#Endpoint for returning delegator number of validator's from given public key   
@api.route('/totalDelegators',methods=['GET'])
def getTotalDelegators():
    pubKey = request.args.get('pubKey', default = 1, type = str)
    validator_object = validator.find_one_by_public_key(pubKey)
    return {"message": f"{pubKey} has {validator_object['delegators_number']} delegators"}




