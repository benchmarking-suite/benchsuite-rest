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
from flask import Blueprint
from flask_restplus import Api

from benchsuite.rest.apiv1 import description
from benchsuite.rest.apiv1 import api as apiv1

blueprint = Blueprint('apiv2', __name__, url_prefix='/api/v2')


api = Api(
    blueprint,
    title='Benchmarking Suite REST API',
    version='2.0',
    description=description,
    # All API metadatas
)

# reuse the same error handlers of apiv1
from benchsuite.rest.apiv1.errors import register_error_handlers
register_error_handlers(api)


from .executions import api as executions_ns
from benchsuite.rest.apiv1.sessions import api as sessions_ns
from benchsuite.rest.apiv1.providers import api as providers_ns
from benchsuite.rest.apiv1.benchmarks import api as benchmarks_ns

api.add_namespace(sessions_ns)
api.add_namespace(executions_ns)
api.add_namespace(providers_ns)
api.add_namespace(benchmarks_ns)
