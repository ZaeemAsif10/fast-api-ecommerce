from pydantic import BaseModel
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float

    model_config = {"from_attributes": True}

class OrderCreate(BaseModel):
    items: list[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    created_at: datetime
    items: list[OrderItemResponse]

    model_config = {"from_attributes": True}