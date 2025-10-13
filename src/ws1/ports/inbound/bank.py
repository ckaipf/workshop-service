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

"""Port definition of a Bank class"""

from abc import ABC, abstractmethod

from pydantic import UUID4

from ws1.models import BankAccount


class BankPort(ABC):
    """An abstract definition of a bank class"""

    @abstractmethod
    async def create_account(self, *, name: str) -> UUID4:
        """Establish an account for the given user with a balance of 0.

        Returns the bank account number as a UUID4.
        """

    @abstractmethod
    async def credit(self, *, account_number: UUID4, amount: float) -> float:
        """Register a credit for the given account number.

        Returns the current account balance as a float.

        Raises:
            `AccountNotFoundError`: If `account_number` does not match an existing
                account.
        """

    @abstractmethod
    async def debit(self, *, account_number: UUID4, amount: float) -> float:
        """Register a debit for the given account number.

        Returns the current account balance as a float.

        Raises:
            `AccountNotFoundError`: If `account_number` does not match an existing
                account.
        """

    @abstractmethod
    async def get_account(self, *, account_number: UUID4) -> BankAccount:
        """Retrieve account info including the name and balance

        Raises:
            `AccountNotFoundError`: If `account_number` does not match an existing
                account.
        """

    # TODO: add account close/delete method
