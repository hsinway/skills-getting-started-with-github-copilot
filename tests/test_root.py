def test_root_redirect(client):
    # Arrange: client fixture
    # Act
    response = client.get("/", allow_redirects=False)
    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"