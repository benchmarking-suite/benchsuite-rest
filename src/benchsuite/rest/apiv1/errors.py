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
from benchsuite.core.model.exception import BashCommandExecutionFailedException, \
    UndefinedSessionException


def handle_custom_exception(error):
    return {'message': str(error)}, 500

def handle_command_failed_exception(error):
    return {'message': str(error), 'stdout': str(error.stdout), 'stderr': str(error.stderr)}, 400

def handle_undefined_session(error):
    return {'message': str(error)}, 400


def register_error_handlers(api):
    api.error_handlers[BashCommandExecutionFailedException] = handle_command_failed_exception
    api.error_handlers[UndefinedSessionException] = handle_undefined_session
    api._default_error_handler = handle_custom_exception