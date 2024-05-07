# game_state_service.py

from flask import Flask, jsonify

app = Flask(__name__)

current_state = {
    'scene_id': None,
    'player_inventory': [],
    'clues_discovered': [],
    'suspects_interrogated': [],
    'game_over': False
}

@app.route('/state', methods=['GET', 'POST'])
def state():
    if request.method == 'GET':
        return jsonify(current_state)
    elif request.method == 'POST':
        data = request.json
        current_state.update(data)
        return jsonify({'message': 'State updated successfully', 'state': current_state})

if __name__ == '__main__':
    app.run(debug=True)
