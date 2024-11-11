products = {}
LOW_STOCK = 5


def login(): 
    try:
        print("Welcome to AFAQ'S inventory management program.")
        
        user = input("Are you user or admin, admin/user: ")
        
        if user == "admin":
            user_name = input("Enter your user name: ")
            user_password = input("Enter your password: ")
            if user_password == "admin":
                print("Login successful!")

                while True:
                    print(f"HI {user_name}, What do you want to perform?")
                    print("1. Add product")
                    print("2. Update product")
                    print("3. Delete product")
                    print("4. View products")
                    print("5. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        product_id = int(input("Enter product ID which you want to add: "))
                        name = input("Enter product name: ")
                        category = input("Enter product category: ")
                        price = float(input("Enter product price: "))
                        stock_quantity = int(input("Enter stock quantity: "))
                        Product.add_product(product_id, name, category, price, stock_quantity)
                    elif choice == 2:
                        product_id = int(input("Enter product ID: "))
                        name = input("Enter product name: ")
                        category = input("Enter product category: ")
                        price = float(input("Enter product price: "))
                        stock_quantity = int(input("Enter stock quantity: "))
                        Product.update_product(product_id, name, category, price, stock_quantity)
                    elif choice == 3:
                        product_id = int(input("Enter product ID to delete: "))
                        Product.delete_product(product_id)
                    elif choice == 4:
                        Product.display_products()
                    elif choice == 5:
                        break
        elif user == "user":
            while True:            
                print("1. View products")
                print("2. Buy any product")
                print("3. Exit")
                choice = int(input("What do you want to perform 1/2 or 3: "))
                if choice == 1:
                    Product.display_products()
                elif choice == 2:
                    Product.display_products()
                    product_id = int(input("Enter product ID which you want to buy: "))
                    quantity = int(input("How much did you want to buy the product: "))
                    Product.buy_product(product_id, quantity)
                elif choice == 3:
                    break
    except ValueError:
        print("Value error")          

class Product():
    @staticmethod
    def add_product(product_id, name, category, price, stock_quantity):
        if product_id in products:
            print(f"Product ID {product_id} already exists. Use a different ID.")
        else:
            products[product_id] = {
                "name": name,
                "category": category,
                "price": price,
                "stock_quantity": stock_quantity
            }
            print(f"Product '{name}' added successfully.")

    @staticmethod
    def delete_product(product_id):
        if product_id in products:
            del products[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found!")

    @staticmethod
    def update_product(product_id, name, category, price, stock_quantity):
        if product_id in products:
            products[product_id]["name"] = name
            products[product_id]["category"] = category
            products[product_id]["price"] = price
            products[product_id]["stock_quantity"] = stock_quantity
            print("Product updated successfully!")
        else:
            print("Product not found!")

    @staticmethod
    def display_products():
        if not products:
            print("No products in inventory.")
            return
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details['name']}, Category: {details['category']}, Price: ${details['price']}, Stock: {details['stock_quantity']}")
            Product.track_stock_levels(product_id)

    @staticmethod
    def buy_product(product_id, quantity):
        if product_id in products:
            product = products[product_id]      
            if product["stock_quantity"] >= quantity:
                product["stock_quantity"] -= quantity
                total_price = product["price"] * quantity
                print(f"Purchased {quantity} of {product['name']} for ${total_price}.")
            else:
                print(f"Not enough stock for {product['name']}. Available: {product['stock_quantity']}.")
            Product.track_stock_levels(product_id)
        else:
            print(f"Product ID {product_id} not found.")

    @staticmethod
    def track_stock_levels(product_id):
        if products[product_id]["stock_quantity"] <= LOW_STOCK:
            print(f"Warning: Stock for '{products[product_id]['name']}' is low (Current stock: {products[product_id]['stock_quantity']}). Please restock!")


Product.add_product(1, "Phones", "accessories", 300 , 20)
Product.add_product(2, "headphones", "accessories", 300 , 20)
Product.add_product(3, "tablets", "accessories", 300 , 20)
Product.add_product(4, "laptop", "accessories", 300 , 20)
Product.add_product(5, "covers", "accessories", 300 , 20)



if __name__ == '__main__':
    login()



