from flask import Flask, render_template, request, redirect
from database import db
from models import Customer, ClickstreamEvent, Transaction
from load_csv import load_csv_data
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///analytics.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create DB + load CSVs once
if not os.path.exists("analytics.db"):
    with app.app_context():
        db.create_all()
    load_csv_data(app)


# -----------------------------
# Customers
# -----------------------------
@app.get("/customers")
def customers_list():
    return render_template(
        "customers.html",
        customers=Customer.query.all()
    )


# -----------------------------
# Clickstream Events
# -----------------------------
@app.get("/clickstream")
def clickstream_list():
    events = ClickstreamEvent.query.order_by(
        ClickstreamEvent.event_timestamp.desc()
    ).limit(200)
    return render_template("clickstream.html", events=events)


# -----------------------------
# Transactions
# -----------------------------
@app.get("/transactions")
def transactions_list():
    txs = Transaction.query.order_by(
        Transaction.event_timestamp.desc()
    ).limit(200)
    return render_template("transactions.html", transactions=txs)


if __name__ == "__main__":
    app.run(debug=True)
