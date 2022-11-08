def test_get_all_breakfasts_with_empty_db_returns_empty_list(client):
    response = client.get("/breakfast")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_bike_with_empty_db_returns_404(client):
    response = client.get("/breakfast/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "msg" in response_body

def test_get_one_bike_with_populated_db_returns_bike_json(client, two_breakfasts):
    response = client.get("/breakfast/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Cap'n Crunch", 
        "rating":3.5, 
        "prep_time":3
    }

def test_post_one_breakfast_creates_breakfast_in_db(client, two_breakfasts):
    response = client.post("/breakfast", json={
        "name": "Scone",
        "rating": 2,
        "prep_time": 1
    })
    response_body = response.get_json()

    assert response.status_code == 201
    # assert "id" in response_body 
    assert response_body == {'msg':f'Sucessfully created Breakfast with id = 3'}