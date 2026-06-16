classDiagram
    class Customer {
        -int customerId
        -String name
        -Transaction[] purchaseHistory
        +getPurchaseHistory() Transaction[]
        +placeOrder(selectedItems: FoodItem[]) Transaction
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

    Customer "1" --> "0..*" Transaction : purchase history
    Customer "1" --> "0..*" Transaction : places
    Transaction "1" *-- "1..*" FoodItem : contains
    ItemCatalog "1" o-- "0..*" FoodItem : lists