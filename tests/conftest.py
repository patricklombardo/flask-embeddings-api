import pytest
from app import app


@pytest.fixture
def client(mocker):
    mocker.patch(
        "embeddings_service.EmbeddingsService.get_status",
        lambda x: True,
    )

    mocker.patch(
        "embeddings_service.EmbeddingsService.generate_embeddings",
        lambda x, y: [0.0, 0.0, 0.0, 0.0],
    )

    app.config["TESTING"] = True
    app.config["DEBUG"] = True
    return app.test_client()


@pytest.fixture
def client_not_ready(mocker):
    mocker.patch(
        "embeddings_service.EmbeddingsService.get_status",
        lambda x: False,
    )

    app.config["TESTING"] = True
    app.config["DEBUG"] = True
    return app.test_client()
