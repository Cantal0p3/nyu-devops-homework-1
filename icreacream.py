# Copyright 2016 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, Response, jsonify, request, json

# Status Codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND = 404
HTTP_409_CONFLICT = 409

# Create Flask application
app = Flask(__name__)

######################################################################
# GET INDEX
######################################################################
@app.route('/')
def index():
    return jsonify(name='My REST API Service', version='1.0', url='/resources'), HTTP_200_OK

######################################################################
# LIST ALL resourceS
######################################################################
@app.route('/flavors', methods=['GET'])
def list_all_flavors():
    # YOUR CODE here (remove pass)
    pass

######################################################################
# RETRIEVE A resource
######################################################################
@app.route('/flavors/flavor/<serialno>', methods=['GET'])
def get_a_flavor(serialno):
    # YOUR CODE here (remove pass)
    pass

######################################################################
# ADD A NEW resource
######################################################################
@app.route('/flavors/flavor', methods=['POST'])
def create_new_flavor():
    # YOUR CODE here (remove pass)
    pass

######################################################################
# UPDATE AN EXISTING resource
######################################################################
@app.route('/flavors/flavor/<serialno>', methods=['PUT'])
def update_flavor(serialno):
    # YOUR CODE here (remove pass)
    pass

######################################################################
# DELETE A resource
######################################################################
@app.route('/flavors/flavor/<serialno>', methods=['DELETE'])
def delete_flavor(serialno):
    # YOUR CODE here (remove pass)
    pass

############################################################################
# QUERY Resources by some attribute of the Resource - Type: Vegan/Non-Vegan
############################################################################
@app.route('/flavors/<attributeValue>', methods=['GET'])
def list_resources_by_type(attributeValue):
    # YOUR CODE here (remove pass)
    pass
    
######################################################################
# PERFORM some Action on the Resource - UPDATE a resource status
######################################################################
@app.route('/flavors/flavor/<serialno>/<statusvalue>', methods=['PUT'])
def update_flavor_status(serialno,statusvalue):
    # YOUR CODE here (remove pass)
    pass

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    # Get bindings from the environment
    port = os.getenv('PORT', '5000')
    app.run(host='0.0.0.0', port=int(port), debug=True)