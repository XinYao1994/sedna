# Copyright 2021 The KubeEdge Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sedna.common.config import Context
from sedna.service.server import AggregationServerv2

from interface import data, trainer, aggregation, transmitter

import os
import logging

def run_server():
    chooser = {
        "per_round": 1
    }
    
    server = AggregationServerv2(
        data = data, 
        trainer=trainer, 
        aggregation=aggregation, 
        transmitter=transmitter, 
        chooser=chooser)
    
    server.start()

if __name__ == '__main__':
    run_server()

