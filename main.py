from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# # порядок важности цветов (пример)
# ORDER = {
#     "red": 0,
#     "green": 1,
#     "blue": 2
# }

@app.route("/sort", methods=["POST"])
def sort_colors():
    data = request.json

    values = data.get("values", [])
    order_rule = data.get("order_rule", {})

    sorted_values = sorted(
        values,
        key=lambda x: int(order_rule.get(x, -1)),
        reverse=True
    )

    return jsonify({
        "sorted": sorted_values
    })

if __name__ == "__main__":
    app.run()