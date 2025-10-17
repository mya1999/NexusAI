# NexusAI Dashboard

An AI-powered dashboard built with modern technologies for real-time data processing, machine learning predictions, and beautiful data visualization.

## 🚀 Features

- **FastAPI Backend**: High-performance REST API with async support
- **React/Next.js Frontend**: Modern, responsive UI with server-side rendering
- **PostgreSQL Database**: Robust relational database for data persistence
- **JWT Authentication**: Secure user authentication and authorization
- **Real-time Data Processing**: WebSocket support for live data updates
- **Machine Learning Integration**: Built-in ML model serving with scikit-learn
- **Docker Containerization**: Easy deployment with Docker Compose
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions

## 📋 Prerequisites

- Docker and Docker Compose (recommended)
- OR:
  - Python 3.11+
  - Node.js 18+
  - PostgreSQL 15+
  - Redis 7+

## 🛠️ Quick Start

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/mya1999/NexusAI.git
cd NexusAI
```

2. Create environment file:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start all services:
```bash
docker-compose up -d
```

4. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Manual Setup

#### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

```
NexusAI/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   ├── core/              # Core functionality (config, security)
│   │   ├── db/                # Database configuration
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   └── ml/                # Machine learning modules
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                   # Next.js frontend
│   ├── src/
│   │   ├── app/               # Next.js app directory
│   │   ├── components/        # React components
│   │   ├── lib/               # Utilities and API client
│   │   └── store/             # State management
│   ├── Dockerfile
│   └── package.json
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD pipeline
├── docker-compose.yml         # Docker Compose configuration
└── README.md
```

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user

### Data
- `GET /api/data/` - Get data points
- `POST /api/data/` - Create data point
- `GET /api/data/stats` - Get statistics

### Machine Learning
- `POST /api/ml/predict` - Make prediction
- `POST /api/ml/train` - Train model
- `GET /api/ml/model-info` - Get model information

### WebSocket
- `WS /api/ws/data` - Real-time data stream

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm run test
npm run lint
```

## 🚀 Deployment

The project includes a CI/CD pipeline configured with GitHub Actions. On push to `main`:

1. Runs backend tests
2. Runs frontend linting
3. Builds Docker images
4. Deploys to your platform (configure as needed)

### Deployment Options

- **Docker Swarm**: Use `docker stack deploy`
- **Kubernetes**: Convert docker-compose.yml with Kompose
- **AWS ECS/EKS**: Push images to ECR
- **Azure Container Instances**: Use Azure Container Registry
- **Google Cloud Run**: Deploy containers directly

## 🔧 Configuration

### Environment Variables

Backend (.env):
```env
DATABASE_URL=postgresql://user:password@host:5432/dbname
SECRET_KEY=your-secret-key
REDIS_URL=redis://host:6379
```

Frontend (.env.local):
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 📊 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Database
- **Redis** - Caching and pub/sub
- **scikit-learn** - Machine learning
- **JWT** - Authentication

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization
- **Zustand** - State management
- **Axios** - HTTP client

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **GitHub Actions** - CI/CD
- **pytest** - Backend testing

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- FastAPI documentation
- Next.js documentation
- scikit-learn community