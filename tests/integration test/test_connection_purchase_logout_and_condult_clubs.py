from tests.conftest import DEFAULT_CLUBS


def test_loggin_and_purchase_places(client):
    response = client.post("/showSummary", data={"email": "kate@shelifts.co.uk"})
    assert response.status_code == 200
    response = client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "She Lifts",
                "places": "1",
            },
        )
    assert response.status_code == 200
    response = client.get("/logout")
    assert response.status_code == 302
    assert response.location == "/"
    response = client.get("/clubsPoints")
    assert response.status_code == 200
    assert response.data
    for club in DEFAULT_CLUBS:
        assert club["name"] in response.data.decode("utf-8")
