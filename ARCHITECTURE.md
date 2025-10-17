# NexusAI Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         NexusAI Dashboard                        │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │────▶│   Backend    │────▶│  PostgreSQL  │
│  Next.js:3000│     │ FastAPI:8000 │     │   Database   │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                      │
       │                    │                      │
       │                    ▼                      │
       │             ┌──────────────┐              │
       │             │    Redis     │              │
       │             │   Cache      │              │
       │             └──────────────┘              │
       │                                           │
       └───────────────────────────────────────────┘
                    WebSocket Connection
```

## Component Details

### Frontend (Next.js)

**Technology Stack:**
- Next.js 14 (React framework)
- TypeScript
- Tailwind CSS
- Recharts (data visualization)
- Zustand (state management)
- Axios (HTTP client)

**Features:**
- Server-side rendering (SSR)
- Client-side routing
- Responsive design
- Real-time updates
- Authentication flow

**Pages:**
- `/` - Landing page with auth redirect
- `/login` - User login
- `/register` - User registration
- `/dashboard` - Main dashboard (protected)

### Backend (FastAPI)

**Technology Stack:**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- Pydantic (data validation)
- Python-JOSE (JWT tokens)
- Passlib (password hashing)
- WebSockets
- scikit-learn (ML)

**API Endpoints:**

```
Authentication:
  POST   /api/auth/register    - Register new user
  POST   /api/auth/login       - Login user
  GET    /api/auth/me          - Get current user

Data Management:
  GET    /api/data/            - List data points
  POST   /api/data/            - Create data point
  GET    /api/data/stats       - Get statistics

Machine Learning:
  POST   /api/ml/predict       - Make prediction
  POST   /api/ml/train         - Train model
  GET    /api/ml/model-info    - Model information

Real-time:
  WS     /api/ws/data          - WebSocket data stream
```

### Database (PostgreSQL)

**Schema:**

```sql
-- Users Table
users
  id              SERIAL PRIMARY KEY
  email           VARCHAR UNIQUE NOT NULL
  username        VARCHAR UNIQUE NOT NULL
  hashed_password VARCHAR NOT NULL
  is_active       BOOLEAN DEFAULT true
  is_superuser    BOOLEAN DEFAULT false
  created_at      TIMESTAMP
  updated_at      TIMESTAMP

-- Data Points Table
data_points
  id          SERIAL PRIMARY KEY
  name        VARCHAR
  value       FLOAT
  category    VARCHAR
  metadata    JSONB
  timestamp   TIMESTAMP
```

### Cache (Redis)

**Purpose:**
- Session management
- Real-time pub/sub
- Caching frequently accessed data
- Rate limiting

## Data Flow

### Authentication Flow

```
1. User submits credentials
   Frontend → POST /api/auth/login

2. Backend validates credentials
   Backend → Query PostgreSQL

3. Generate JWT token
   Backend → Create signed token

4. Return token to client
   Backend → Frontend

5. Store token locally
   Frontend → localStorage

6. Include token in requests
   Frontend → Authorization: Bearer <token>
```

### Real-time Data Flow

```
1. Client connects to WebSocket
   Frontend → WS /api/ws/data

2. Backend accepts connection
   WebSocket Manager

3. Backend streams data
   Every 2 seconds → Client

4. Frontend updates UI
   React state update → Re-render
```

### ML Prediction Flow

```
1. User requests prediction
   Frontend → POST /api/ml/predict

2. Backend loads model
   MLService → joblib.load()

3. Make prediction
   Model → predict(features)

4. Return result
   Backend → Frontend

5. Display prediction
   Frontend → Update UI
```

## Security Architecture

### Authentication

```
┌──────────────┐
│   Password   │
└──────┬───────┘
       │
       ▼
  [Bcrypt Hash]
       │
       ▼
┌──────────────┐
│   Database   │
└──────────────┘
```

### Authorization

```
┌──────────────┐
│  JWT Token   │
└──────┬───────┘
       │
       ▼
[Verify Signature]
       │
       ▼
┌──────────────┐
│ Extract User │
└──────┬───────┘
       │
       ▼
[Check Permissions]
```

## Deployment Architecture

### Development

```
┌─────────────────────────────────────┐
│         Docker Compose              │
│  ┌──────────┐  ┌──────────┐        │
│  │ Frontend │  │ Backend  │        │
│  │   :3000  │  │  :8000   │        │
│  └──────────┘  └──────────┘        │
│                                     │
│  ┌──────────┐  ┌──────────┐        │
│  │PostgreSQL│  │  Redis   │        │
│  │  :5432   │  │  :6379   │        │
│  └──────────┘  └──────────┘        │
└─────────────────────────────────────┘
```

### Production

```
┌─────────────────────────────────────┐
│         Load Balancer               │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────┐   ┌───▼────┐
│Frontend│   │Frontend│
│  Node  │   │  Node  │
└───┬────┘   └───┬────┘
    │            │
    └──────┬─────┘
           │
    ┌──────▼──────┐
    │   API GW    │
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────┐   ┌───▼────┐
│Backend │   │Backend │
│FastAPI │   │FastAPI │
└───┬────┘   └───┬────┘
    │            │
    └──────┬─────┘
           │
    ┌──────▼──────┐
    │             │
┌───▼────┐   ┌───▼────┐
│  RDS   │   │ Redis  │
│Postgres│   │Cluster │
└────────┘   └────────┘
```

## CI/CD Pipeline

```
┌─────────────┐
│ Git Push    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│GitHub Actions│
└──────┬──────┘
       │
       ├──▶ Lint Code
       ├──▶ Run Tests
       ├──▶ Build Docker Images
       ├──▶ Security Scan
       │
       ▼
┌─────────────┐
│   Deploy    │
└─────────────┘
```

## Monitoring & Logging

```
Application Logs
    │
    ▼
┌─────────────┐
│  Backend    │──▶ stdout/stderr
└─────────────┘
    │
    ▼
┌─────────────┐
│   Docker    │──▶ docker logs
└─────────────┘
    │
    ▼
┌─────────────┐
│ Log Service │
│(ELK/Splunk) │
└─────────────┘
```

## Scaling Strategy

### Horizontal Scaling

- Frontend: Multiple Next.js instances
- Backend: Multiple FastAPI workers
- Database: Read replicas
- Redis: Cluster mode

### Vertical Scaling

- Increase container resources
- Optimize database queries
- Add caching layers

## Technology Choices

### Why FastAPI?
- High performance (async support)
- Automatic API documentation
- Type validation with Pydantic
- Modern Python 3.11+ features

### Why Next.js?
- SSR for better SEO
- Excellent developer experience
- Built-in routing
- Optimal performance

### Why PostgreSQL?
- ACID compliance
- Rich feature set
- JSON support
- Excellent performance

### Why Docker?
- Consistent environments
- Easy deployment
- Isolation
- Scalability

## Performance Considerations

- Connection pooling (SQLAlchemy)
- Query optimization (indexes)
- Caching strategies (Redis)
- Async I/O (FastAPI)
- Code splitting (Next.js)
- Image optimization
- CDN for static assets
