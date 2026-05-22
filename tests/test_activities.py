import src.app as app_module


def test_get_activities_returns_expected(client):
    # Arrange
    activity_name = "Chess Club"
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert activity_name in data


def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert resp.status_code == 200
    assert email in app_module.activities[activity]["participants"]


def test_signup_already_registered_returns_400(client):
    # Arrange
    activity = "Chess Club"
    existing_email = "michael@mergington.edu"
    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing_email})
    # Assert
    assert resp.status_code == 400


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    # Act
    resp = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert resp.status_code == 200
    assert email not in app_module.activities[activity]["participants"]


def test_unregister_not_registered_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "not_registered@mergington.edu"
    # Act
    resp = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert resp.status_code == 404


def test_activity_not_found_returns_404_for_signup_and_unregister(client):
    # Arrange
    missing = "Nonexistent Activity"
    email = "someone@mergington.edu"
    # Act
    resp_signup = client.post(f"/activities/{missing}/signup", params={"email": email})
    resp_unregister = client.delete(f"/activities/{missing}/unregister", params={"email": email})
    # Assert
    assert resp_signup.status_code == 404
    assert resp_unregister.status_code == 404
