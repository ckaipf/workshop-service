from typing import Annotated

from fastapi import Depends
from ghga_service_commons.api.di import DependencyDummy

from ws1.ports.inbound.bank import BankPort

bank_port = DependencyDummy("bank_port")

BankDummy = Annotated[
    BankPort, Depends(bank_port)
]
