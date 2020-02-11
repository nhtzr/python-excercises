from typing import Iterable

from .data import GoodsItem, Receipt, ReceiptItem
from .rules import calculate_sales_tax


def generate_receipt_item(item: GoodsItem) -> ReceiptItem:
    tax = calculate_sales_tax(item)
    net_price = item.price + tax
    return ReceiptItem(
        tax=tax,
        net_price=net_price,
        **item._asdict())


def generate_receipt(items: Iterable[GoodsItem]) -> Receipt:
    receipt_items = list(generate_receipt_item(item) for item in items)
    sales_taxes = sum(item.tax for item in receipt_items)
    total = sum(item.net_price for item in receipt_items)
    return Receipt(
        total=total,
        sales_taxes=sales_taxes,
        items=receipt_items)


def receipt_repr(receipt: Receipt):
    lines = (
        *(f"{i.quantity} {i.description}: {i.net_price:0.2f}" for i in receipt.items),
        f"Sales Taxes: {receipt.sales_taxes:0.2f}",
        f"Total: {receipt.total:0.2f}")
    return str.join('\n', lines)
