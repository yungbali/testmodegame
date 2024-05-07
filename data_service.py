# data_service.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game_data.db'
db = SQLAlchemy(app)

class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

# Create database tables
db.create_all()

@app.route('/scenes', methods=['GET', 'POST'])
def scenes():
    if request.method == 'GET':
        scenes = Scene.query.all()
        return jsonify([scene.to_dict() for scene in scenes])
    elif request.method == 'POST':
        data = request.json
        scene = Scene(name=data['name'], description=data['description'])
        db.session.add(scene)
        db.session.commit()
        return jsonify({'message': 'Scene created successfully', 'scene': scene.to_dict()})

if __name__ == '__main__':
    app.run(debug=True)
