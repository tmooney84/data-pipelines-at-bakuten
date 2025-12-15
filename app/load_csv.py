import csv
from datetime import datetime
from pathlib import Path

from models import db, Customer, ClickstreamEvent, Transaction


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def load_csv_data(app):
    with app.app_context():

        # 🔒 Prevent duplicate ingestion
        if Customer.query.first():
            print("📦 CSV data already loaded — skipping ingestion.")
            return

        print("📥 Loading CSV data...")

        load_customers()
        load_clickstream()
        load_transactions()

        print("✅ CSV ingestion complete.")


def load_customers():
    path = DATA_DIR / "customers.csv"

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            customer = Customer(
                customer_id=row["customer_id"],
                signup_date=datetime.strptime(
                    row["signup_date"], "%Y-%m-%d"
                ).date(),
                country=row["country"],
                segment=row["segment"],
                lifetime_value=float(row["lifetime_value"]),
                is_vip=row["is_vip"].lower() == "true",
                marketing_opt_in=row["marketing_opt_in"].lower() == "true",
            )
            db.session.add(customer)

        db.session.commit()


def load_clickstream():
    path = DATA_DIR / "clickstream.csv"

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            event = ClickstreamEvent(
                event_id=row["event_id"],
                customer_id=row["customer_id"],
                session_id=row["session_id"],
                event_timestamp=datetime.fromisoformat(
                    row["event_timestamp"]
                ),
                event_type=row["event_type"],
                page=row["page"],
                device=row["device"],
                traffic_source=row["traffic_source"],
                campaign=row["campaign"],
                country=row["country"],
                product_category=row["product_category"],
            )
            db.session.add(event)

        db.session.commit()


def load_transactions():
    path = DATA_DIR / "transactions.csv"

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            tx = Transaction(
                transaction_id=row["transaction_id"],
                customer_id=row["customer_id"],
                event_timestamp=datetime.fromisoformat(
                    row["event_timestamp"]
                ),
                channel=row["channel"],
                product_category=row["product_category"],
                payment_method=row["payment_method"],
                status=row["status"],
                gross_amount=float(row["gross_amount"]),
                discount_amount=float(row["discount_amount"]),
                tax_amount=float(row["tax_amount"]),
                net_amount=float(row["net_amount"]),
            )
            db.session.add(tx)

        db.session.commit()
