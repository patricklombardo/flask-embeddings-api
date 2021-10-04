from embeddings_service import EmbeddingsService


def test_load_embeddings_service():
    """ "Tests that embeddings service loads correctly"""
    es = EmbeddingsService()
    # Assert status is false on init
    assert es.get_status() is False
    # Load service
    es.load_embed_service()
    # Assert
    assert es.get_status() is True


def test_generate_embedings():
    """Tests that embeddings are correctly
    Note this does not test the 'correctness' of the response as this is would be a test of the TensorFlow model
    """
    es = EmbeddingsService()
    # Init Service
    es.load_embed_service()
    test_sentence = "the quick brown fox jumps over the lazy dog"
    # Get Response
    res = es.generate_embeddings([test_sentence])
    # Assert
    assert type(res) is list
    assert res is not None


def test_get_status():
    """Tests get_status returns false before load"""
    es = EmbeddingsService()
    status = es.get_status()

    assert status is False
