import pytest

from models import Customer, FoodItem, ItemCatalog, Transaction


def make_sample_catalog() -> ItemCatalog:
    catalog = ItemCatalog()
    catalog.add_item(FoodItem(1, "Spicy Burger", 8.99, "Entrees", 4.6))
    catalog.add_item(FoodItem(2, "Large Soda", 2.49, "Drinks", 4.1))
    catalog.add_item(FoodItem(3, "Vanilla Shake", 5.50, "Drinks", 4.8))
    catalog.add_item(FoodItem(4, "Fries", 3.99, "Sides", 4.3))
    return catalog


# Should compute the exact total for a transaction containing multiple items.
def test_calculate_total_with_multiple_items() -> None:
    burger = FoodItem(1, "Spicy Burger", 8.99, "Entrees", 4.6)
    soda = FoodItem(2, "Large Soda", 2.49, "Drinks", 4.1)
    transaction = Transaction(1001, [burger, soda])

    assert transaction.compute_total() == 11.48


# Should reject empty item selections so invalid empty orders are not processed.
def test_order_total_rejects_empty_selection() -> None:
    with pytest.raises(ValueError, match="selected_items cannot be empty"):
        Transaction(1002, [])


# Should return only items from the requested category, ignoring case and spacing.
def test_filter_by_category_returns_matching_items() -> None:
    catalog = make_sample_catalog()

    drinks = catalog.filter_by_category("  drinks ")

    assert [item.name for item in drinks] == ["Large Soda", "Vanilla Shake"]


# Should sort menu items alphabetically by name for predictable browsing.
def test_sort_by_name_orders_items_alphabetically() -> None:
    catalog = make_sample_catalog()

    names = [item.name for item in catalog.sort_by_name()]

    assert names == ["Fries", "Large Soda", "Spicy Burger", "Vanilla Shake"]


# Should sort menu items by descending price when descending=True.
def test_sort_by_price_descending() -> None:
    catalog = make_sample_catalog()

    names = [item.name for item in catalog.sort_by_price(descending=True)]

    assert names == ["Spicy Burger", "Vanilla Shake", "Fries", "Large Soda"]


# Should track purchase history and verify user only after a successful order.
def test_customer_verify_user_depends_on_purchase_history() -> None:
    customer = Customer(5001, "Avery")
    assert customer.verify_user() is False

    catalog = make_sample_catalog()
    order = customer.place_order(catalog.filter_by_category("Drinks"))

    assert order.get_item_count() == 2
    assert order.compute_total() == 7.99
    assert customer.verify_user() is True
