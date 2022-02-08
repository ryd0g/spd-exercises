# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
def discount(base_price):
    if base_price > 1000:
        return 0.95
    else:
        return 0.85

def get_price(quantity, item_price):
    base_price = quantity * item_price
    discount_factor = discount(base_price)
    return base_price * discount_factor

print(discount(500))
print(get_price(2, 700))