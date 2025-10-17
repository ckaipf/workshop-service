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


"""FastAPI endpoint function definitions"""

from uuid import uuid4

from fastapi import APIRouter, status

from ws1.adapters.inbound.fastapi_.dummy import BankDummy

router = APIRouter()


@router.get(
    "/health",
    summary="health",
    status_code=status.HTTP_200_OK,
)
async def health():
    """Used to test if this service is alive"""
    return {"status": "OK"}


@router.post(
    "/accounts",
    summary="Create account",
    status_code=status.HTTP_200_OK,
)
async def create_account(bank: BankDummy):
    """Used to create a new account"""
    account_id = await bank.create_account()
    return {"account_id": account_id}

@router.get(
    "/accounts/{account_id}",
    summary="Get account",
    status_code=status.HTTP_200_OK,
)
async def get_account(account_id: str):
    """Used to get account details"""
    return {"account_id": account_id}

