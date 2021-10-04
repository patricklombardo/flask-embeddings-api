from flask import Flask, request, jsonify
from scipy import spatial
from cerberus import Validator

from embeddings_service import EmbeddingsService
from helpers import (
    embeddings_bulk_schema,
    embeddings_similarity_schema,
    invalid_json_response,
    invalid_query_param,
    service_not_ready_response,
)

# Init App
app = Flask(__name__)

# Init Embeddings Service
embeddings_service = EmbeddingsService()

# Check if Embeddings Service is ready before serving requests
@app.before_request
def check_service_status():
    service_status = embeddings_service.get_status()
    if service_status is False:
        return service_not_ready_response


@app.route("/embeddings", methods=["GET"])
def get_embeddings():
    sentence = request.args.get("sentence")
    if sentence is None or type(sentence) is not str:
        return invalid_query_param

    embeddings = embeddings_service.generate_embeddings([sentence])

    response = {"embedding": embeddings}
    return jsonify(response)


@app.route("/embeddings/bulk", methods=["POST"])
def post_embeddings_bulk():
    request_json = request.json

    # Validate Request JSON
    v = Validator(embeddings_bulk_schema)
    if not v.validate(request_json):
        return invalid_json_response

    sentences = request_json.get("sentences")
    embeddings = embeddings_service.generate_embeddings(sentences)

    response = {"embeddings": embeddings}
    return jsonify(response)


@app.route("/embeddings/similarity", methods=["POST"])
def post_embeddings_similarity():
    request_json = request.json
    v = Validator(embeddings_similarity_schema)
    if not v.validate(request_json):
        return invalid_json_response

    sentence_1 = request.json.get("sentence_1")
    sentence_2 = request.json.get("sentence_2")

    embedding_1 = embeddings_service.generate_embeddings([sentence_1])
    embedding_2 = embeddings_service.generate_embeddings([sentence_2])

    # Calculate similarity = 1 - (distance)
    similarity = 1.0 - spatial.distance.cosine(embedding_1, embedding_2)
    return jsonify({"similarity": similarity})


if __name__ == "__main__":
    # Load Embeddings Service
    embeddings_service.load_embed_service()

    # Run app
    app.run()
