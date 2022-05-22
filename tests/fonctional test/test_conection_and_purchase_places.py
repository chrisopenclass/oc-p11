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
