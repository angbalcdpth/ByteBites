"""Temporary scenario script for ByteBites model behavior checks.

Exercises item addition, menu sorting, category filtering,
and order total computation with simple assertions.
"""

from models import Customer, FoodItem, ItemCatalog


def assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}. Expected {expected}, got {actual}")


if __name__ == "__main__":
    burger = FoodItem(1, "Spicy Burger", 8.99, "Entrees", 4.6)
    soda = FoodItem(2, "Large Soda", 2.49, "Drinks", 4.1)
    shake = FoodItem(3, "Vanilla Shake", 5.50, "Drinks", 4.8)
    fries = FoodItem(4, "Fries", 3.99, "Sides", 4.3)

    catalog = ItemCatalog()
    catalog.add_item(burger)
    catalog.add_item(soda)
    catalog.add_item(shake)
    catalog.add_item(fries)

    drinks = catalog.filter_by_category("drinks")
    assert_equal([item.name for item in drinks], ["Large Soda", "Vanilla Shake"], "Category filter failed")

    by_name = catalog.sort_by_name()
    assert_equal([item.name for item in by_name], ["Fries", "Large Soda", "Spicy Burger", "Vanilla Shake"], "Name sort failed")

    by_price_desc = catalog.sort_by_price(descending=True)
    assert_equal([item.name for item in by_price_desc], ["Spicy Burger", "Vanilla Shake", "Fries", "Large Soda"], "Price sort failed")

    by_popularity = catalog.sort_by_popularity()
    assert_equal([item.name for item in by_popularity], ["Vanilla Shake", "Spicy Burger", "Fries", "Large Soda"], "Popularity sort failed")

    customer = Customer(5001, "Avery")
    order = customer.place_order([burger, soda, fries])

    assert_equal(order.get_item_count(), 3, "Order item count failed")
    assert_equal(order.compute_total(), 15.47, "Order total failed")
    assert_equal(customer.verify_user(), True, "User verification failed")

    print("Category filter (Drinks):", [item.name for item in drinks])
    print("Sorted by name:", [item.name for item in by_name])
    print("Sorted by price desc:", [item.name for item in by_price_desc])
    print("Sorted by popularity:", [item.name for item in by_popularity])
    print("Order total:", order.compute_total())
    print("All scenario checks passed.")
