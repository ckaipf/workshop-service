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

"""Concrete implementation of a Bank class"""


from uuid import uuid4

from pydantic import UUID4

from ws1.models import BankAccount
from ws1.ports.inbound.bank import BankPort
from ws1.ports.outbound.DAO import AccountDaoPort


class Bank(BankPort):
    """Concrete implementation of a Bank class"""

    def __init__(self, *, account_dao: AccountDaoPort) -> None:
        self._account_dao = account_dao


    async def create_account(self) -> UUID4:
        """Establish an account for the given user with a balance of 0."""
        account_id = uuid4()
        bank_account = BankAccount(account_number=account_id, balance=0.0)
        await self._account_dao.insert(bank_account)
        print(f"Creating account for {account_id}")
        return account_id

    async def credit(self, *, account_number: UUID4, amount: float) -> float:
        pass

    async def debit(self, *, account_number: UUID4, amount: float) -> float:
        pass

    async def get_account(self, *, account_number: UUID4) -> float:
        pass