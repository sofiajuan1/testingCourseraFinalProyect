@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    if name:
        results = Product.find_by_name(name)
        return jsonify([p.serialize() for p in results]), 200
    # ... otras condiciones
