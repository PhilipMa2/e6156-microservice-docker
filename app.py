from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Ma19690022@acadmate-db.csmdb1acis22.us-east-2.rds.amazonaws.com:3306/acadmate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.VARCHAR(200), nullable=False)
    requestee_id = db.Column(db.VARCHAR(200), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    __table_args__ = (
        UniqueConstraint('requester_id', 'requestee_id', name='unique_request'),
    )

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return '<h1>Hello from flask</h1>'

@app.route("/team/applied/<int:student_id>", methods=["GET"])
def read_team_applied(student_id):
    teams = Team.query.filter(Team.requester_id == student_id, Team.confirmed.is_(False))
    if teams:
        teams_list = [
            {
                'team_id': team.team_id,
                'requester_id': team.requester_id,
                'requestee_id': team.requestee_id,
                'confirmed': team.confirmed,
            }
            for team in teams
        ]
        return jsonify(teams_list)
    return jsonify({"message": "Team not found"}), 404

@app.route("/team/received/<int:student_id>", methods=["GET"])
def read_team_received(student_id):
    teams = Team.query.filter(Team.requestee_id == student_id, Team.confirmed.is_(False))
    if teams:
        teams_list = [
            {
                'team_id': team.team_id,
                'requester_id': team.requester_id,
                'requestee_id': team.requestee_id,
                'confirmed': team.confirmed,
            }
            for team in teams
        ]
        return jsonify(teams_list)
    return jsonify({"message": "Team not found"}), 404

@app.route("/team/formed/<int:student_id>", methods=["GET"])
def read_team_formed(student_id):
    teams = Team.query.filter((Team.requester_id == student_id) | (Team.requestee_id == student_id), Team.confirmed.is_(True))
    if teams:
        teams_list = [
            {
                'team_id': team.team_id,
                'requester_id': team.requester_id,
                'requestee_id': team.requestee_id,
                'confirmed': team.confirmed,
            }
            for team in teams
        ]
        return jsonify(teams_list)
    return jsonify({'message': 'Team not found'}), 404

@app.route("/team", methods=["POST"])
def create_team():
    try:
        data = request.get_json()
        new_team = Team(
            requester_id=data.get("requester_id"),
            requestee_id=data.get("requestee_id")
        )
        db.session.add(new_team)
        db.session.commit()

        return jsonify({'message': 'Team created successfully'}), 201
    except Exception as e:
        print(f"Error creating team: {str(e)}")
        return jsonify({"error": "An error occurred during team creation"}), 500

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
