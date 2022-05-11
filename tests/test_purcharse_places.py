def test_not_more_than_12_places(client):
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "13",
        },
    )
    assert response.status_code == 200
    assert "you can&#39;t buy more than 12 places!" in response.data.decode("utf-8")


def test_not_more_than_remaining_places(client):
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "2",
        },
    )

    assert response.status_code == 200

    assert (
        "your trying to buy more places than avalaible places  !"
        in response.data.decode("utf-8")
    )


def test_not_more_than_remaining_points(client_with_no_points):
    response = client_with_no_points.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "1",
        },
    )
    assert response.status_code == 200

    assert (
        "you can&#39;t buy more places than your avalaible places !"
        in response.data.decode("utf-8")
    )


def test_can_buy_places(client):
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "1",
        },
    )
    assert response.status_code == 200

    assert "Great-booking complete!" in response.data.decode("utf-8")


# TODO Write test sending non-existant competition name
# TODO Write test sending non-existant club name
# TODO Write test sending a non-integer places number
