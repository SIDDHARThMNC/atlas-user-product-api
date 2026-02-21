from fastapi import FastAPI, HTTPException
from app.schemas import UserCreate, UserResponse, ProductCreate, ProductResponse
from app.database import users_collection, products_collection

app = FastAPI(title="Atlas User & Product Management API")

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    user_dict = user.model_dump()
    users_collection.insert_one(user_dict)
    return user_dict

@app.get("/users/{email}", response_model=UserResponse)
def get_user(email: str):
    user = users_collection.find_one({"email": email}, {"_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    existing_product = products_collection.find_one({"sku": product.sku})
    if existing_product:
        raise HTTPException(status_code=400, detail="SKU already exists")
    
    product_dict = product.model_dump()
    products_collection.insert_one(product_dict)
    return product_dict

@app.get("/products/{sku}", response_model=ProductResponse)
def get_product(sku: str):
    product = products_collection.find_one({"sku": sku}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
