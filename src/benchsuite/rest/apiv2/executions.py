# Benchmarking Suite
# Copyright 2014-2017 Engineering Ingegneria Informatica S.p.A.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Developed in the ARTIST EU project (www.artist-project.eu) and in the
# CloudPerfect EU project (https://cloudperfect.eu/)
from flask_restplus import Resource

from benchsuite.rest.apiv1.executions import api as apiv1, \
    execution_command_info_model

api = apiv1



@api.route('/<string:exec_id>/run')
class ExecutionRunAction(Resource):

    @api.marshal_with(execution_command_info_model, code=200, description='Runs the run commands')
    def post(self, exec_id):
        return "OK"
