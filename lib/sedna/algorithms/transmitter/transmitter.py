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

from abc import ABC, abstractmethod


class AbstractTransmitter(ABC):

    @abstractmethod
    def recv(self):
        pass

    @abstractmethod
    def send(self, data):
        pass


class WSTransmitter(AbstractTransmitter, ABC):

    def recv(self):
        pass

    def send(self, data):
        pass


class S3Transmitter(AbstractTransmitter, ABC):

    def __init__(self,
                 s3_bucket,
                 s3_endpoint_url,
                 access_key,
                 secret_key):
        self.s3_bucket = s3_bucket
        self.s3_endpoint_url = s3_endpoint_url
        self.access_key = access_key
        self.secret_key = secret_key

    def recv(self):
        pass

    def send(self, data):
        pass
