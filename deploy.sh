#!/bin/bash

# Deployment script for NexusAI Dashboard
# This script can be customized for your deployment environment

set -e

echo "🚀 Starting NexusAI deployment..."

# Pull latest changes
echo "📥 Pulling latest code..."
git pull origin main

# Build and start containers
echo "🐳 Building Docker containers..."
docker-compose build

echo "🏃 Starting services..."
docker-compose up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check service health
echo "🔍 Checking service health..."
docker-compose ps

echo "✅ Deployment complete!"
echo "Frontend: http://localhost:3000"
echo "Backend: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
