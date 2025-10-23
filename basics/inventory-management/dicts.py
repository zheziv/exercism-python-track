"""Functions to keep track and alter inventory."""
from collections import Counter


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    """
    counts = []
    for x in items:
        counts.append(x.count(x))
        # x.count(x) is trying to call the string method .count()
        # — which counts characters inside the string (e.g., "iron".count("iron") → 1).
        # It does not count how many times "iron" appears in the list items. So it always returns 1 for every element.
    return dict(zip(items, counts))
    """
    return Counter(items)


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    counts = create_inventory(items)
    return dict(Counter(inventory) + Counter(counts))



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    c2 = create_inventory(items)
    c1 = Counter(inventory)
    ''' Notice Counter automatically removes any keys that reach zero or go negative.
    e.g. dict(Counter(a) - Counter(b))
    If you want to keep keys with zero values (like "diamond": 0), you need a tiny modification below.
    '''
    # max(c1[k] - c2[k], 0) clamps negatives to 0
    ''' It only takes keys in inventory when the item from items doesn't exist in inventory.
    So it need to use c1.keys() rather than c1.keys() | c2.keys().
    e.g. {"iron": 3, "gold": 2}, ["iron", "wood", "iron", "diamond"] => the expected = {"iron": 1, "gold": 2}
    '''
    return {k : max(c1[k] - c2[k], 0) for k in c1.keys()}



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    result = inventory.pop(item, None)
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    result = []
    for k, v in inventory.items():
        if v > 0:
            result.append((k, v))
    return result
