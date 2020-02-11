from decimal import Decimal

from .data import GoodsItem


def parse_good_item_line(full_item_line: str) -> GoodsItem:
    price_sep = ' at '
    quantity_separator = ' '

    *description_tokens, price_tokens = full_item_line.split(price_sep)
    description_line = str.join(price_sep, description_tokens)
    price = Decimal(price_tokens.strip())

    quantity_token, *description_tokens = description_line.split(quantity_separator)
    quantity = int(quantity_token)
    description = str.join(quantity_separator, description_tokens)

    try:
        description.index('imported')
        imported = True
    except ValueError:
        imported = False

    return GoodsItem(
        price=price,
        imported=imported,
        description=description,
        quantity=quantity
    )
