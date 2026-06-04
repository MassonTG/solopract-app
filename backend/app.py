from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "shop"),
        user=os.getenv("DB_USER", "shop"),
        password=os.getenv("DB_PASSWORD", "shop123")
    )

@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, description FROM products ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "price": float(r[2]), "description": r[3]} for r in rows])

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, description) VALUES (%s, %s, %s) RETURNING id",
                (data["name"], data["price"], data.get("description", "")))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": new_id, "name": data["name"], "price": data["price"]}), 201

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)