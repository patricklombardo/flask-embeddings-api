from flask import Response

# Cerberus Schemas
embeddings_bulk_schema = {"sentences": {"type": "list", "required": True}}
embeddings_similarity_schema = {
    "sentence_1": {"type": "string", "required": True},
    "sentence_2": {"type": "string", "required": True},
}

# Responses
invalid_json_response = Response(status=400, response="Invalid request JSON")
invalid_query_param = Response(status=400, response="Invalid or missing parameter")
service_not_ready_response = Response(
    status=503, response="Service unavailable - Embeddings service is loading..."
)
