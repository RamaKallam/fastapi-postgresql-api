# This is an in-memory database used for CRUD operations (data will reset on restart)
from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Fast api web framework!"

products = [
Product(id= 1, name= "phone", description= "budget phone", price= 99, quantity= 10),
Product(id= 2, name= "laptop", description= "gaming laptop", price= 990, quantity= 6)
]

# Fetch all products
@app.get("/products")
def get_all_products():
    return products

# Fetch product by its Id
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"

# Add a product
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

# Update a product
@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i]= product
            return "Product updated successfully"
    return "Product not found"

# Delete a Product
@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"    
        
    return "Product not found"    