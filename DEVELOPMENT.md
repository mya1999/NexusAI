# NexusAI Development Guide

## Getting Started

This guide will help you set up the development environment for NexusAI.

## Prerequisites

- Docker Desktop (for containerized development)
- Python 3.11+ (for backend development)
- Node.js 18+ (for frontend development)
- Git

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mya1999/NexusAI.git
cd NexusAI
```

### 2. Backend Development

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp ../.env.example .env

# Run the development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at http://localhost:8000
API documentation at http://localhost:8000/docs

### 3. Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will be available at http://localhost:3000

## Running with Docker

```bash
# Build and start all services
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Database Management

### Migrations

```bash
cd backend

# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Testing

### Backend Tests

```bash
cd backend
pytest
pytest -v  # Verbose output
pytest --cov  # With coverage
```

### Frontend Tests

```bash
cd frontend
npm run lint
npm run test  # If you add tests
```

## Code Style

### Backend
- Follow PEP 8
- Use type hints
- Document functions with docstrings

### Frontend
- Use TypeScript
- Follow ESLint rules
- Use functional components

## Project Architecture

### Backend Structure

```
backend/
├── app/
│   ├── api/            # API routes
│   ├── core/           # Config and security
│   ├── db/             # Database setup
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   └── main.py         # Application entry
```

### Frontend Structure

```
frontend/
├── src/
│   ├── app/            # Next.js pages
│   ├── components/     # React components
│   ├── lib/            # Utilities
│   └── store/          # State management
```

## API Development

### Adding a New Endpoint

1. Create schema in `backend/app/schemas/`
2. Create model in `backend/app/models/` (if needed)
3. Create endpoint in `backend/app/api/endpoints/`
4. Register router in `backend/app/api/router.py`
5. Add tests

### Example:

```python
# schemas/item.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str

# api/endpoints/items.py
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/")
async def create_item(item: ItemCreate):
    return {"item": item}
```

## Frontend Development

### Creating a New Page

1. Create file in `src/app/[page-name]/page.tsx`
2. Add to navigation if needed
3. Style with Tailwind CSS

### Using the API

```typescript
import { api } from '@/lib/api';

const fetchData = async () => {
  const response = await api.get('/endpoint');
  return response.data;
};
```

## Environment Variables

### Backend
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
SECRET_KEY=your-secret-key
REDIS_URL=redis://localhost:6379
```

### Frontend
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Troubleshooting

### Database Connection Issues
- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Check database credentials

### Frontend Build Issues
- Clear node_modules: `rm -rf node_modules && npm install`
- Clear Next.js cache: `rm -rf .next`

### Docker Issues
- Clear containers: `docker-compose down -v`
- Rebuild: `docker-compose up --build`

## Contributing

1. Create a feature branch
2. Make changes
3. Write tests
4. Run tests and linting
5. Submit pull request

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
