from decimal import Decimal
from typing import NamedTuple, List


class GoodsItem(NamedTuple):
    price: Decimal
    imported: bool
    description: str
    quantity: int


class ReceiptItem(NamedTuple):
    price: Decimal
    imported: bool
    description: str
    quantity: int
    tax: Decimal
    net_price: Decimal


class Receipt(NamedTuple):
    sales_taxes: int
    total: int
    items: List[ReceiptItem]
