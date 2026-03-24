from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

## This constructor is not required pydantic will take care
    # def __init__(self, id, name, description, price, quantity):
    #     self.id = id    
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity