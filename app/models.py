from database import db
from datetime import datetime


# -----------------------------
# Customers
# -----------------------------
class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.String(20), primary_key=True)
    signup_date = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(5))
    segment = db.Column(db.String(50))
    lifetime_value = db.Column(db.Float)
    is_vip = db.Column(db.Boolean)
    marketing_opt_in = db.Column(db.Boolean)

    # Relationships
    click_events = db.relationship("ClickstreamEvent", back_populates="customer")
    transactions = db.relationship("Transaction", back_populates="customer")


# -----------------------------
# Clickstream Events
# -----------------------------
class ClickstreamEvent(db.Model):
    __tablename__ = "clickstream_events"

    event_id = db.Column(db.String(36), primary_key=True)
    customer_id = db.Column(
        db.String(20),
        db.ForeignKey("customers.customer_id"),
        nullable=False
    )
    session_id = db.Column(db.String(50))
    event_timestamp = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(db.String(50))
    page = db.Column(db.String(100))
    device = db.Column(db.String(50))
    traffic_source = db.Column(db.String(50))
    campaign = db.Column(db.String(100))
    country = db.Column(db.String(5))
    product_category = db.Column(db.String(100))

    customer = db.relationship("Customer", back_populates="click_events")


# -----------------------------
# Transactions
# -----------------------------
class Transaction(db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column(db.String(20), primary_key=True)
    customer_id = db.Column(
        db.String(20),
        db.ForeignKey("customers.customer_id"),
        nullable=False
    )
    event_timestamp = db.Column(db.DateTime, nullable=False)
    channel = db.Column(db.String(50))
    product_category = db.Column(db.String(100))
    payment_method = db.Column(db.String(50))
    status = db.Column(db.String(50))

    gross_amount = db.Column(db.Float)
    discount_amount = db.Column(db.Float)
    tax_amount = db.Column(db.Float)
    net_amount = db.Column(db.Float)

    customer = db.relationship("Customer", back_populates="transactions")
