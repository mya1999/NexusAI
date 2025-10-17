# NexusAI Quick Start Guide

Get NexusAI up and running in 5 minutes!

## Prerequisites

- Docker Desktop installed and running
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/mya1999/NexusAI.git
cd NexusAI
```

### 2. Start the Application

```bash
# Start all services with Docker Compose
docker compose up -d
```

This will start:
- PostgreSQL database (port 5432)
- Redis cache (port 6379)
- FastAPI backend (port 8000)
- Next.js frontend (port 3000)

### 3. Wait for Services

Wait ~30 seconds for all services to initialize.

### 4. Access the Application

Open your browser and navigate to:
- **Frontend**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **API**: http://localhost:8000

## First Steps

### Register a New User

1. Go to http://localhost:3000
2. Click "Register"
3. Enter your email, username, and password
4. Click "Register"

### Login

1. Go to http://localhost:3000/login
2. Enter your credentials
3. Click "Sign in"

### Explore the Dashboard

Once logged in, you'll see:
- **Statistics Cards**: Total data points, averages, min/max values
- **Data Trends Chart**: Visual representation of data
- **ML Model Info**: Current model version and accuracy
- **Make Prediction**: Test the ML model with random features

## Stopping the Application

```bash
docker compose down
```

To remove all data (including database):
```bash
docker compose down -v
```

## Troubleshooting

### Port Already in Use

If you get "port already in use" errors:

```bash
# Find what's using the port
lsof -i :3000  # for frontend
lsof -i :8000  # for backend

# Stop the process or change ports in docker-compose.yml
```

### Services Not Starting

Check logs:
```bash
docker compose logs -f
```

Check specific service:
```bash
docker compose logs backend
docker compose logs frontend
```

### Database Connection Issues

Restart services:
```bash
docker compose restart
```

## Next Steps

- Read the [Development Guide](DEVELOPMENT.md)
- Check the [API Documentation](http://localhost:8000/docs)
- Review the [Security Policy](SECURITY.md)
- See the [Changelog](CHANGELOG.md)

## Need Help?

- Check the main [README](README.md)
- Review logs: `docker compose logs -f`
- Open an issue on GitHub

## Default Configuration

- Database: `nexusai` / `nexusai123`
- Secret Key: `your-secret-key-change-in-production-12345`
- **⚠️ Change these in production!**
