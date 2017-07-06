#!/usr/bin/env python
# BenchmarkingSuite - Benchmarking Controller
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
import logging
import signal
import sys

from flask import Flask

from benchsuite.rest.apiv1 import blueprint as blueprint1

app = Flask(__name__)


#app.config.SWAGGER_UI_JSONEDITOR = True

app.register_blueprint(blueprint1)

def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)
    signal.signal(signal.SIGINT, func)

def on_exit(sig, func=None):
    print('Exiting...')
    sys.exit(1)


if __name__ == '__main__':
    set_exit_handler(on_exit)

    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stdout)

    print('Using internal server. Not use this in production!!!')
    app.run(debug=True)
