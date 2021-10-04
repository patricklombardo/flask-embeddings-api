# Flask Embeddings API
A simple API that encodes sentences using Google's [`universal-sentence-encoder`](https://tfhub.dev/google/universal-sentence-encoder/4).

# Usage
### /embeddings?sentence=[sentence]
Method: `GET`

URL Params: Required: `sentence=[string]`

Data Params: None

Success Response: 

    - Code: 200
    - Content: `{"embedding": [<int>...]`

Error Response:

    - Code: 503 SERVICE UNAVAILABLE
    - Content: Service unavailable - Embeddings service is loading...

    - Code: 400 BAD REQUEST
    - Content: Invalid or missing parameter

### /embeddings/bulk
Method: `POST`

URL Params: None

Data Params: Required:
```
{'sentences': [<str>...]}
```

Success Response: 

    - Code: 200
    - Content: `{"embeddings": [[<int>...]...]`

Error Response:

    - Code: 503 SERVICE UNAVAILABLE
    - Content: Service unavailable - Embeddings service is loading...

    - Code: 400 BAD REQUEST
    - Content: Invalid request JSON

### /embeddings/bulk
Method: `POST`

URL Params: None

Data Params: Required:
```
{
    'sentence_1': <str>,
    'sentence_2': <str>
    
}
```

Success Response: 

    - Code: 200
    - Content: `{"embeddings": [[<int>...]...]`

Error Response:

    - Code: 503 SERVICE UNAVAILABLE
    - Content: Service unavailable - Embeddings service is loading...

    - Code: 400 BAD REQUEST
    - Content: Invalid request JSON

# Install
```bash
# clone the repository
git clone https://github.com/patricklombardo/flask-embeddings-api.git
cd flask-embeddings-api
# Create your virtualenv if desired
# python -m venv
# . venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

# Run
```bash
export FLASK_APP=flask_embeddings_api
export FLASK_ENV=development
python app.py
```

# Test
Testing is done with pytest and pytest-mock

## Run tests
```bash
python -m pytest
```

## Coverage
```bash
# Run coverage
coverage run -m pytest
# Generate report
coverage report
# Generate HTML report
coverage html
```