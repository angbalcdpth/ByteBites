"""
ByteBites core model classes:
- Customer: stores customer identity and purchase history, and can place orders.
- FoodItem: represents a menu item with name, price, category, and popularity rating.
- ItemCatalog: manages the full collection of food items and supports category filtering.
- Transaction: groups selected items for one order and computes total cost.
"""

from __future__ import annotations

from datetime import date


class Customer:
    def __init__(self, customer_id: int, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.purchase_history: list[Transaction] = []

    def get_purchase_history(self) -> list[Transaction]:
        return list(self.purchase_history)

    def place_order(self, selected_items: list[FoodItem]) -> Transaction:
        if not selected_items:
            raise ValueError("Cannot place order with no items")
        transaction_id = len(self.purchase_history) + 1
        transaction = Transaction(transaction_id, selected_items)
        self.purchase_history.append(transaction)
        return transaction

    def verify_user(self) -> bool:
        return self.customer_id > 0 and bool(self.name.strip())


class FoodItem:
    def __init__(
        self,
        item_id: int,
        name: str,
        price: float,
        category: str,
        popularity_rating: float,
    ) -> None:
        if price < 0:
            raise ValueError("price must be non-negative")
        if not (0 <= popularity_rating <= 5):
            raise ValueError("popularity_rating must be between 0 and 5")
        if not name.strip():
            raise ValueError("name cannot be empty")
        if not category.strip():
            raise ValueError("category cannot be empty")

        self.item_id = item_id
        self.name = name
        self.price = float(price)
        self.category = category
        self.popularity_rating = float(popularity_rating)

    def get_details(self) -> str:
        return (
            f"{self.name} ({self.category}) - ${self.price:.2f}, "
            f"rating {self.popularity_rating:.1f}/5"
        )


class ItemCatalog:
    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def get_all_items(self) -> list[FoodItem]:
        return list(self.items)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        target = category.strip().lower()
        return [item for item in self.items if item.category.lower() == target]

    def add_item(self, item: FoodItem) -> None:
        if any(existing.item_id == item.item_id for existing in self.items):
            raise ValueError(f"item_id {item.item_id} already exists")
        self.items.append(item)

    def remove_item(self, item_id: int) -> None:
        for index, item in enumerate(self.items):
            if item.item_id == item_id:
                del self.items[index]
                return
        raise ValueError(f"item_id {item_id} not found")


class Transaction:
    def __init__(
        self,
        transaction_id: int,
        selected_items: list[FoodItem],
        transaction_date: date | None = None,
    ) -> None:
        if not selected_items:
            raise ValueError("selected_items cannot be empty")

        self.transaction_id = transaction_id
        self.transaction_date = transaction_date or date.today()
        self.selected_items = list(selected_items)

    def compute_total(self) -> float:
        return round(sum(item.price for item in self.selected_items), 2)

    def get_item_count(self) -> int:
        return len(self.selected_items)
