import pandas as pd
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

# Create a sample DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Item 1', 'Item 2', 'Item 3'],
    'value': [100, 200, 300]
})

@api.route('/api/items', methods=['GET'])
def get_items():
    """
    Returns all items from the DataFrame as a JSON list.
    """
    # Convert the entire DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')
    return jsonify(data)

@api.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Returns a single item by its ID from the DataFrame.
    If the item is not found, returns a 404 error.
    """
    # Filter the DataFrame by the provided item_id
    item = df[df['id'] == item_id]
    if item.empty:
        return jsonify({"error": f"Item {item_id} not found"}), 404
    # Get the first (and only) matching record as a dictionary
    data = item.to_dict(orient='records')[0]
    return jsonify(data)
