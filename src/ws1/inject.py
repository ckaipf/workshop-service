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

"""Dependency injection and preparation"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ws1.adapters.inbound.fastapi_.configure import get_configured_app
from ws1.config import Config

# @asynccontextmanager
# async def prepare_core(
#     *,
#     config: Config,
#     account_dao_override: AccountDao | None = None,
# ) -> AsyncGenerator[BankPort]:
#     """Constructs and initializes all core components and their outbound dependencies.

#     The _override parameter can be used to override the default dependencies.
#     """


# def prepare_core_with_override(
#     *, config: Config, bank_override: BankPort | None = None
# ):
#     """Resolve the `bank_override` context manager based on config and override (if any)."""
#     return (
#         nullcontext(bank_override)
#         if bank_override
#         else prepare_core(config=config)
#     )


@asynccontextmanager
async def prepare_rest_app(*, config: Config) -> AsyncGenerator[FastAPI]:
    """Construct and initialize an REST API app along with all its dependencies.
    By default, the core dependencies are automatically prepared but you can also
    provide them using the bank_override parameter.
    """
    app = get_configured_app(config=config)
    yield app
