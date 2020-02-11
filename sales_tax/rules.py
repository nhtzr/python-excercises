from decimal import Decimal
from math import ceil

from .data import GoodsItem


def is_book(item: GoodsItem) -> bool:
    return item.description.find('book') != -1


def is_food(item: GoodsItem) -> bool:
    return item.description.find('chocolate') != -1


def is_medical(item: GoodsItem) -> bool:
    return item.description.find('pill') != -1


def is_exempt(item: GoodsItem):
    return any(cond(item)
               for cond in (is_book, is_food, is_medical))


def is_imported(item: GoodsItem):
    return item.imported


def calculate_basic_sales_tax(item: GoodsItem):
    # except books, food, and medical products that are exempt
    if is_exempt(item):
        return 0

    # Basic sales tax is applicable at a rate of 10% on all goods
    return 10


def calculate_import_duty_tax(item: GoodsItem):
    # Import duty is an additional sales tax applicable on all imported goods at a rate of 5%,
    # with no exemptions.
    if is_imported(item):
        return 5

    return 0


def calculate_sales_tax(item: GoodsItem, round_base=5):
    basic = calculate_basic_sales_tax(item)
    duty = calculate_import_duty_tax(item)
    n_rate = sum((basic, duty))
    np_rate = n_rate * item.price
    rounded_np_rate = ceil(np_rate / round_base) * round_base
    final_price = rounded_np_rate / 100
    return Decimal(final_price)
