# API Testing Guide

This guide shows you how to test the NexusAI API endpoints.

## Using FastAPI Swagger UI (Recommended)

1. Start the backend: `docker compose up backend`
2. Open http://localhost:8000/docs
3. Try out endpoints interactively

## Using cURL

### Health Check

```bash
curl http://localhost:8000/health
```

### Register a User

```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "testpass123"
  }'
```

### Login

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpass123"
  }'
```

Save the returned `access_token` for authenticated requests.

### Get Current User (Authenticated)

```bash
TOKEN="your-access-token-here"
curl http://localhost:8000/api/auth/me \
  -H "Authorization: Bearer $TOKEN"
```

### Create Data Point (Authenticated)

```bash
TOKEN="your-access-token-here"
curl -X POST http://localhost:8000/api/data/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test-data",
    "value": 42.5,
    "category": "test",
    "metadata": {"source": "api-test"}
  }'
```

### Get Data Points (Authenticated)

```bash
TOKEN="your-access-token-here"
curl http://localhost:8000/api/data/ \
  -H "Authorization: Bearer $TOKEN"
```

### Get Statistics (Authenticated)

```bash
TOKEN="your-access-token-here"
curl http://localhost:8000/api/data/stats \
  -H "Authorization: Bearer $TOKEN"
```

### ML Prediction (Authenticated)

```bash
TOKEN="your-access-token-here"
curl -X POST http://localhost:8000/api/ml/predict \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [0.5, 0.7, 0.3]
  }'
```

### Get ML Model Info (Authenticated)

```bash
TOKEN="your-access-token-here"
curl http://localhost:8000/api/ml/model-info \
  -H "Authorization: Bearer $TOKEN"
```

## Using Python Requests

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Register
response = requests.post(f"{BASE_URL}/auth/register", json={
    "email": "test@example.com",
    "username": "testuser",
    "password": "testpass123"
})
print(response.json())

# Login
response = requests.post(f"{BASE_URL}/auth/login", json={
    "email": "test@example.com",
    "password": "testpass123"
})
token = response.json()["access_token"]

# Authenticated request
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{BASE_URL}/data/stats", headers=headers)
print(response.json())
```

## WebSocket Testing

### Using wscat

```bash
npm install -g wscat
wscat -c ws://localhost:8000/api/ws/data
```

### Using Python

```python
import asyncio
import websockets

async def test_websocket():
    uri = "ws://localhost:8000/api/ws/data"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

asyncio.run(test_websocket())
```

## Running Backend Tests

```bash
cd backend
pip install -r requirements.txt
pytest -v
```

## Expected Responses

### Successful Registration (201)

```json
{
  "email": "test@example.com",
  "username": "testuser",
  "id": 1,
  "is_active": true,
  "created_at": "2024-01-01T00:00:00"
}
```

### Successful Login (200)

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Statistics Response (200)

```json
{
  "total_count": 42,
  "average_value": 127.5,
  "min_value": 10.0,
  "max_value": 500.0
}
```

### ML Prediction Response (200)

```json
{
  "prediction": 3.456,
  "confidence": 0.95,
  "model_version": "1.0.0"
}
```

## Error Responses

### Unauthorized (401)

```json
{
  "detail": "Could not validate credentials"
}
```

### Not Found (404)

```json
{
  "detail": "Resource not found"
}
```

### Validation Error (422)

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Load Testing

Using Apache Bench:

```bash
# Test login endpoint
ab -n 100 -c 10 -T "application/json" \
  -p login.json \
  http://localhost:8000/api/auth/login
```

## Tips

- Use the Swagger UI for interactive testing
- Save your access token for authenticated requests
- Check logs: `docker compose logs backend -f`
- Test WebSocket connections for real-time features
- Run pytest for automated testing
