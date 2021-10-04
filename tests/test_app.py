from cerberus import Validator

# Embeddings mock response
generate_embeddings_mock_response = [0.0, 0.0, 0.0, 0.0]


def test_client_handles_service_not_ready(client_not_ready):
    """Tests for 503 response if embeddings service is not ready"""
    url = "/embeddings?sentence=the+quick+brown+fox"
    response = client_not_ready.get(url)
    assert response.status == "503 SERVICE UNAVAILABLE"
    assert response.data == b"Service unavailable - Embeddings service is loading..."


def test_get_embeddings_works(client):
    """Test URL: GET /embeddings?sentence={sentence}
    Tests simple embedding via query params"""
    url = "/embeddings?sentence=the+quick+brown+fox"

    response = client.get(url)
    json_response = response.get_json()

    response_schema = {"embedding": {"type": "list", "required": True}}
    v = Validator(response_schema)
    assert v.validate(json_response) is True
    assert json_response == {"embedding": generate_embeddings_mock_response}


def test_get_embeddings_handles_bad_input(client):
    """Test URL: GET /embeddings
    Tests simple embedding handles bad input"""
    url = "/embeddings"

    response = client.get(url)

    assert response.status == "400 BAD REQUEST"
    assert response.data == b"Invalid or missing parameter"


def test_post_bulk_embeddings_works(client):
    """Test URL: POST /embeddings/bulk
    Tests bulk works
    """

    url = "/embeddings/bulk"
    data = {"sentences": ["the quick brown fox", "jumps over the lazy dog"]}
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    response = client.post(url, json=data, headers=headers)
    json_response = response.get_json()

    response_schema = {"embeddings": {"type": "list", "required": True}}
    v = Validator(response_schema)
    assert v.validate(json_response) is True
    assert json_response == {"embeddings": generate_embeddings_mock_response}


def test_post_bulk_embeddings_handles_bad_input(client):
    """Test URL: POST /embeddings/bulk
    Tests bulk handles bad input
    """
    url = "/embeddings/bulk"
    data = {"bad_input": {"i like": ["to"], "break": "things"}}
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    response = client.post(url, json=data, headers=headers)

    assert response.status == "400 BAD REQUEST"
    assert response.data == b"Invalid request JSON"


def test_post_similarity_works(client):
    """Test URL: POST /embeddings/similarity
    Tests similarity works
    """
    url = "/embeddings/similarity"
    data = {
        "sentence_1": "the quick brown fox",
        "sentence_2": "jumps over the lazy dog",
    }
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    response = client.post(url, json=data, headers=headers)
    json_response = response.get_json()

    response_schema = {"similarity": {"type": "number", "required": True}}
    v = Validator(response_schema)
    assert v.validate(json_response) is True
    # Assert similarity == 1 (e.g. same vector is mocked as response for both sentences)
    # Note: Ignore 0 division warning (expected)
    assert json_response["similarity"] == 1


def test_post_similarity_handles_bad_input(client):
    """Test URL: POST /embeddings/similarity
    Tests similarity handles bad input
    """
    url = "/embeddings/similarity"
    data = {"bad_input": {"i like": ["to"], "break": "things"}}
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    response = client.post(url, json=data, headers=headers)

    assert response.status == "400 BAD REQUEST"
    assert response.data == b"Invalid request JSON"
