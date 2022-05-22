import pytest

from unittest.mock import patch
from gudlft.server import createapp


DEFAULT_CLUBS = [
    {"name": "Simply Lift", "email": "john@simplylift.co", "points": "39"},
    {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
    {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
]

DEFAULT_COMPETITIONS = [
    {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"},
    {"name": "Fall Classic", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"},
]


@pytest.fixture
def client():
    with patch("gudlft.server.loadClubs") as clubs:
        clubs.return_value = DEFAULT_CLUBS

        with patch("gudlft.server.loadCompetitions") as comps:
            comps.return_value = [
                {
                    "name": "Spring Festival",
                    "date": "2022-01-01 00:00:00",
                    "numberOfPlaces": "1",
                }
            ]

            app = createapp({"TESTING": True})
            with app.test_client() as client:
                yield client


@pytest.fixture
def client_with_no_points():
    with patch("gudlft.server.loadClubs") as clubs:
        clubs.return_value = [
            {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "0",
            }
        ]
        with patch("gudlft.server.loadCompetitions") as comps:
            comps.return_value = DEFAULT_COMPETITIONS

            app = createapp({"TESTING": True})
            with app.test_client() as client:
                yield client
