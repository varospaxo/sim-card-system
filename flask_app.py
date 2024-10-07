from flask import Flask, request, jsonify, send_from_directory, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='')

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Use the environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SimCard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sim_number = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Enum('active', 'inactive'), nullable=False, default='inactive')
    activation_date = db.Column(db.DateTime, nullable=True)  # Corresponding to timestamp, can be NULL

# @app.before_first_request
# def create_tables():
#     db.create_all()  # Create database tables

# Serve the index.html file at the root route
@app.route('/', methods=['GET'])
def serve_index():
    return render_template('index.html')

# Add a new SIM card
@app.route('/add-sim', methods=['POST'])
def add_sim():
    data = request.json
    sim_number = data.get('sim_number')
    phone_number = data.get('phone_number')

    if not sim_number or not phone_number:
        return jsonify({"error": "SIM number and phone number are required"}), 400

    # Check if the SIM number already exists
    if SimCard.query.filter_by(sim_number=sim_number).first():
        return jsonify({"error": "SIM number already exists"}), 400

    new_sim = SimCard(sim_number=sim_number, phone_number=phone_number, status='inactive')
    db.session.add(new_sim)
    db.session.commit()
    return jsonify({"message": "SIM card added successfully"}), 201

# Activate SIM
@app.route('/activate', methods=['POST'])
def activate_sim():
    data = request.json
    sim_number = data.get('sim_number')
    if not sim_number:
        return jsonify({"error": "SIM number is required"}), 400

    sim = SimCard.query.filter_by(sim_number=sim_number).first()

    if not sim:
        return jsonify({"error": "SIM card not found"}), 404
    if sim.status == 'active':
        return jsonify({"error": "SIM is already active"}), 400

    sim.status = 'active'
    sim.activation_date = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "SIM activated successfully"}), 200

# Deactivate SIM
@app.route('/deactivate', methods=['POST'])
def deactivate_sim():
    data = request.json
    sim_number = data.get('sim_number')
    if not sim_number:
        return jsonify({"error": "SIM number is required"}), 400

    sim = SimCard.query.filter_by(sim_number=sim_number).first()

    if not sim:
        return jsonify({"error": "SIM card not found"}), 404
    if sim.status == 'inactive':
        return jsonify({"error": "SIM is already inactive"}), 400

    sim.status = 'inactive'
    sim.activation_date = None
    db.session.commit()
    return jsonify({"message": "SIM deactivated successfully"}), 200

# Get SIM details
@app.route('/sim-details/<sim_number>', methods=['GET'])
def get_sim_details(sim_number):
    sim = SimCard.query.filter_by(sim_number=sim_number).first()

    if not sim:
        return jsonify({"error": "SIM card not found"}), 404

    return jsonify({
        "sim_number": sim.sim_number,
        "phone_number": sim.phone_number,
        "status": sim.status,
        "activation_date": sim.activation_date
    }), 200

@app.route('/test', methods=['GET'])
def test():
    return "Flask app is working!"

if __name__ == '__main__':
    app.run(debug=True)