# Atlas User & Product Management API

FastAPI backend connected to MongoDB Atlas for managing Users and Products.

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and add your MongoDB Atlas connection string
3. Build and run with Docker:

```bash
docker build -t atlas-api .
docker run -p 8000:8000 -e MONGO_URL="your_mongodb_url" atlas-api
```

## API Endpoints

### Users
- `POST /users` - Create a new user
- `GET /users/{email}` - Get user by email

### Products
- `POST /products` - Create a new product
- `GET /products/{sku}` - Get product by SKU

## Testing

Access Swagger UI at: `http://localhost:8000/docs`
