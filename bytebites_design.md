classDiagram
    class Customer {
        -int customerId
        -String name
        +getPurchaseHistory() Transaction[]
        +placeOrder(items: FoodItem[]) Transaction
        +verifyUser() bool
    }

    class FoodItem {
        -int itemId
        -String name
        -float price
        -String category
        -float popularityRating
        +getDetails() String
    }

    class ItemCatalog {
        -FoodItem[] items
        +getAllItems() FoodItem[]
        +filterByCategory(category: String) FoodItem[]
        +addItem(item: FoodItem) void
        +removeItem(itemId: int) void
    }

    class Transaction {
        -int transactionId
        -Date transactionDate
        -FoodItem[] selectedItems
        +computeTotal() float
        +getItemCount() int
    }

    Customer "1" --> "many" Transaction : has purchase history
    Transaction "many" *-- "many" FoodItem : contains
    ItemCatalog "1" *-- "many" FoodItem : manages
    Customer "1" --> "1" Transaction : places