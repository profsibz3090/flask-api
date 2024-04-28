from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

epl_teams = {
    "arsenal": {
        "name": "Arsenal",
        "city": "London",
        "stadium": "Emirates Stadium",
        "recent-trophy": "FA Cup (2020-21)"
    },
    "aston-villa": {
        "name": "Aston Villa",
        "city": "Birmingham",
        "stadium": "Villa Park",
        "recent-trophy": "League Cup (1995-96)"
    },
    "brentford": {
        "name": "Brentford",
        "city": "London",
        "stadium": "Brentford Community Stadium",
        "recent-trophy": "Promoted to Premier League (2020-21)"
    },
    "brighton-hove-albion": {
        "name": "Brighton & Hove Albion",
        "city": "Brighton & Hove",
        "stadium": "Falmer Stadium (Amex Stadium)",
        "recent-trophy": "Promoted to Premier League (2016-17)"
    },
    "burnley": {
        "name": "Burnley",
        "city": "Burnley",
        "stadium": "Turf Moor",
        "recent-trophy": "N/A"
    },
    "chelsea": {
        "name": "Chelsea",
        "city": "London",
        "stadium": "Stamford Bridge",
        "recent-trophy": "UEFA Champions League (2020-21)"
    },
    "crystal-palace": {
        "name": "Crystal Palace",
        "city": "London",
        "stadium": "Selhurst Park",
        "recent-trophy": "N/A"
    },
    "everton": {
        "name": "Everton",
        "city": "Liverpool",
        "stadium": "Goodison Park",
        "recent-trophy": "N/A"
    },
    "leeds-united": {
        "name": "Leeds United",
        "city": "Leeds",
        "stadium": "Elland Road",
        "recent-trophy": "N/A"
    },
    "leicester-city": {
        "name": "Leicester City",
        "city": "Leicester",
        "stadium": "King Power Stadium",
        "recent-trophy": "FA Cup (2020-21)"
    },
    "liverpool": {
        "name": "Liverpool",
        "city": "Liverpool",
        "stadium": "Anfield",
        "recent-trophy": "Premier League (2019-20)"
    },
    "manchester-city": {
        "name": "Manchester City",
        "city": "Manchester",
        "stadium": "Etihad Stadium",
        "recent-trophy": "Premier League (2020-21)"
    },
    "manchester-united": {
        "name": "Manchester United",
        "city": "Manchester",
        "stadium": "Old Trafford",
        "recent-trophy": "Premier League (2012-13)"
    },
    "newcastle-united": {
        "name": "Newcastle United",
        "city": "Newcastle upon Tyne",
        "stadium": "St. James' Park",
        "recent-trophy": "N/A"
    },
    "norwich-city": {
        "name": "Norwich City",
        "city": "Norwich",
        "stadium": "Carrow Road",
        "recent-trophy": "Promoted to Premier League (2020-21)"
    },
    "southampton": {
        "name": "Southampton",
        "city": "Southampton",
        "stadium": "St. Mary's Stadium",
        "recent-trophy": "N/A"
    },
    "tottenham-hotspur": {
        "name": "Tottenham Hotspur",
        "city": "London",
        "stadium": "Tottenham Hotspur Stadium",
        "recent-trophy": "League Cup (2007-08)"
    },
    "watford": {
        "name": "Watford",
        "city": "Watford",
        "stadium": "Vicarage Road",
        "recent-trophy": "Promoted to Premier League (2021-22)"
    },
    "west-ham-united": {
        "name": "West Ham United",
        "city": "London",
        "stadium": "London Stadium",
        "recent-trophy": "N/A"
    },
    "wolverhampton-wanderers": {
        "name": "Wolverhampton Wanderers",
        "city": "Wolverhampton",
        "stadium": "Molineux Stadium",
        "recent-trophy": "N/A"
    }
}

class Epl(Resource):
    def get(self,team_id):
        return epl_teams[str(team_id).lower()]
    
class Test(Resource):
    def get():
        return 'Tirimo'

api.add_resource(Epl, '/team/<string:team_id>')
api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(debug=True)