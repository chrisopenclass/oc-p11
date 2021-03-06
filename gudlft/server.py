import json
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def createapp(config=None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
    app.secret_key = "something_special"

    competitions = loadCompetitions()
    clubs = loadClubs()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/showSummary", methods=["POST"])
    def showSummary():
        mail = request.form["email"]
        for club in clubs:
            if mail == club["email"]:
                return render_template("welcome.html", club=club, competitions=competitions)
        flash("l'email est invalide")
        return redirect(url_for("index"))

    @app.route("/book/<competition>/<club>")
    def book(competition, club):
        foundClub = [c for c in clubs if c["name"] == club][0]
        foundCompetition = [c for c in competitions if c["name"] == competition][0]
        if foundClub and foundCompetition:
            return render_template(
                "booking.html", club=foundClub, competition=foundCompetition
            )
        else:
            flash("Something went wrong-please try again")
            return render_template("welcome.html", club=club, competitions=competitions)

    @app.route("/purchasePlaces", methods=["POST"])
    def purchasePlaces():
        competition = [c for c in competitions if c["name"] == request.form["competition"]][
            0
        ]
        club = [c for c in clubs if c["name"] == request.form["club"]][0]
        placesRequired = int(request.form["places"]) * 3
        if placesRequired > int(club['points']):
            flash("you can't buy more places than your avalaible places !")
            return render_template("welcome.html", club=club, competitions=competitions)
        if placesRequired / 3 > 12:
            flash("you can't buy more than 12 places!")
            return render_template("welcome.html", club=club, competitions=competitions)
        if placesRequired / 3 > int(competition["numberOfPlaces"]):
            flash("your trying to buy more places than avalaible places  !")
            return render_template("welcome.html", club=club, competitions=competitions)
        club['points'] = int(club['points']) - placesRequired
        competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - placesRequired / 3
        flash(f'Great-booking complete! you just bought {request.form["places"]}')
        return render_template("welcome.html", club=club, competitions=competitions)

    @app.route('/clubsPoints')
    def display_clubs_points():
        return render_template('clubs.html', clubs=clubs)

    @app.route("/logout")
    def logout():
        return redirect(url_for("index"))
    return app
