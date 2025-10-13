# Copyright 2021 - 2025 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
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

"""Unit tests for the HTTP API"""

import pytest
from ghga_service_commons.api.testing import AsyncTestClient

from tests.fixtures.config import get_config
from ws1.inject import prepare_rest_app

pytestmark = pytest.mark.asyncio()


async def test_health():
    """Test that the health endpoint returns a 200"""
    config = get_config()
    async with (
        prepare_rest_app(config=config) as app,
        AsyncTestClient(app=app) as rest_client,
    ):
        response = await rest_client.get("/health")
        assert response.status_code == 200
