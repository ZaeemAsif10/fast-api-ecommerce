from sqlalchemy import Integer, ForeignKey, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from datetime import datetime, timezone

class OrderSchema(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, default="pending", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user = relationship("UserSchema", backref="orders")
    items = relationship("OrderItemSchema", backref="order")

class OrderItemSchema(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    product = relationship("ProductSchema", backref="order_items")