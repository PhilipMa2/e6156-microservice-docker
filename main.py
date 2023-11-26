from fastapi import FastAPI, HTTPException

app = FastAPI()

teams_db = []

class Team:
    def __init__(self, team_id, requester_id, requestee_id):
        self.team_id = team_id
        self.requester_id = requester_id
        self.requestee_id = requestee_id
        self.confirmed = False

@app.get("/team/{student_id}")
def read_team(student_id: int):
    for entry in teams_db:
        if student_id in [entry.requester_id, entry.requestee_id]:
            return entry
    raise HTTPException(status_code=404, detail="Team not found")

@app.post("/team/")
def create_team(team_id: int, requester_id: int, requestee_id: int):
    new_team = Team(team_id=team_id, requester_id=requester_id, requestee_id=requestee_id)
    teams_db.append(new_team)
    return new_team

@app.put("/team/{team_id}")
def confirm_team(team_id: int):
    for entry in teams_db:
        if entry.team_id == team_id:
            entry.confirmed = True
            return {"message": "Team confirmed"}
    raise HTTPException(status_code=404, detail="Team not found")

@app.delete("/team/{team_id}")
def delete_team(team_id: int):
    for entry in teams_db:
        if entry.team_id == team_id:
            teams_db.remove(entry)
            return {"message": "Team deleted"}
    raise HTTPException(status_code=404, detail="Team not found")
