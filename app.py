from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Ma19690022@database-1.csmdb1acis22.us-east-2.rds.amazonaws.com:3306/teams'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.before_request
def log_request_info():
    app.logger.info('Request Headers: %s', request.headers)
    app.logger.info('Request Body: %s', request.get_data())

@app.after_request
def log_response_info(response):
    app.logger.info('Response Status Code: %s', response.status_code)
    app.logger.info('Response Body: %s', response.get_data())
    return response 

class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer)
    requestee_id = db.Column(db.Integer)
    confirmed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return '<h1>Hello from flask</h1>'

@app.route("/team/<int:student_id>", methods=["GET"])
def read_team(student_id):
    team = Team.query.filter((Team.requestee_id == student_id) | (Team.requestee_id == student_id)).first()
    if team:
        return jsonify(team.__dict__)
    return jsonify({"message": "Team not found"}), 404

@app.route("/team", methods=["POST"])
def create_team():
    data = request.get_json()
    new_team = Team(
        requester_id=data.get("requester_id"),
        requestee_id=data.get("requestee_id")
    )
    db.session.add(new_team)
    db.session.commit()

    return jsonify(new_team.__dict__), 201

@app.route("/team/<int:team_id>", methods=["PUT"])
def confirm_team(team_id):
    team = Team.query.get(team_id)
    if team:
        team.confirmed = True
        db.session.commit()
        return jsonify({"message": "Team confirmed"})
    return jsonify({"message": "Team not found"}), 404

@app.route("/team/<int:team_id>", methods=["DELETE"])
def delete_team(team_id):
    team = Team.query.get(team_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return jsonify({"message": "Team deleted"})
    return jsonify({"message": "Team not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)
