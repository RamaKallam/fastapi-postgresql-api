from fastapi import Depends,FastAPI
from models import Product
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"]

)

# create tables automatically by alchemy
database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "Welcome to Fast api web framework!"

products = [
Product(id= 1, name= "phone", description= "budget phone", price= 99, quantity= 10),
Product(id= 2, name= "laptop", description= "gaming laptop", price= 990, quantity= 6)
]

def get_db():
    db = SessionLocal()
    try:
      yield db
    finally:  
      db.close()

def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            # model_dump give the dictionary and convert into key-value pair as unpacking
            db.add(database_models.Product(**product.model_dump()))
            db.close()
        db.commit()

init_db()

# Fetch all products
@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

# Fetch product by its Id
@app.get("/product/{id}")
def get_product_by_id(id: int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
       return db_product
    return "Product not found"

# Add a product
@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

# Update a product
@app.put("/product/{id}")
def update_product(id: int, product: Product,  db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.quantity = product.quantity
        db_product.price = product.price
        db.commit()
        return "Product updated!"
    else:       
        return "Product not found"

# Delete a Product
@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
       db.delete(db_product)
       db.commit()
       return "Product Deleted" 
    else:    
       return "Product not found"    