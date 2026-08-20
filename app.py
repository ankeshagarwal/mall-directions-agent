from flask import Flask, request, jsonify
from flask_cors import CORS
from mall_agent import MallDirectionsAgent

app = Flask(__name__)
CORS(app)

agent = MallDirectionsAgent()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response = agent.chat(user_message)
    return jsonify({"response": response})

@app.route('/api/stores', methods=['GET'])
def get_stores():
    """Get all stores"""
    stores = []
    for store in agent.stores.values():
        stores.append({
            "name": store.name,
            "floor": store.floor,
            "section": store.section,
            "category": store.category
        })
    return jsonify({"stores": stores})

@app.route('/api/store/<store_name>', methods=['GET'])
def get_store(store_name):
    """Get specific store information"""
    info = agent.get_store_info(store_name)
    return jsonify(info)

@app.route('/api/directions', methods=['POST'])
def get_directions():
    """Get directions to a store"""
    data = request.json
    store_name = data.get('store', '')
    from_location = data.get('from', 'current location')
    
    directions = agent.get_directions(from_location, store_name)
    return jsonify(directions)

@app.route('/api/category/<category>', methods=['GET'])
def stores_by_category(category):
    """Get stores by category"""
    stores = agent.find_stores_by_category(category)
    return jsonify({"category": category, "stores": stores})

@app.route('/api/emergency', methods=['GET'])
def emergency_contacts():
    """Get emergency contacts"""
    return jsonify(agent.get_emergency_contacts())

@app.route('/api/map', methods=['GET'])
def mall_map():
    """Get mall map and layout"""
    return jsonify(agent.get_mall_map())

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "online"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
