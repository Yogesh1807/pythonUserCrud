uvicorn app.main:app --host 0.0.0.0 --port 8000

# UserCrud Project Documentation

## Overview

**UserCrud** is a FastAPI-based RESTful API for managing users with full CRUD (Create, Read, Update, Delete) operations. It uses PostgreSQL as the database and SQLModel as the ORM. The project is structured for scalability and maintainability.

---

## Project Structure

```
UserCrud/
│
├── app/
│   ├── main.py                # FastAPI app entry point
│   ├── routes/
│   │   └── user_route.py      # User API endpoints
│   ├── services/
│   │   └── user_service.py    # Business logic for users
│   ├── repositories/
│   │   └── user_repository.py # Database access for users
│   ├── schemas/
│   │   └── user.py            # Pydantic models for request/response
│   ├── models/
│   │   └── user.py            # SQLModel ORM models
│   └── db/
│       └── session.py         # Database session management
│
├── .env                       # Environment variables (DB connection)
└── requirements.txt           # Python dependencies
```

---

## Environment Setup

1. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

2. **Configure Database**

   - Ensure PostgreSQL is running.
   - Create a database named `mydb`.
   - Set credentials in `.env`:
     ```
     DATABASE_URL=postgresql://postgres:root@localhost:5432/mydb
     ```

3. **Run the Application**
   ```
   uvicorn app.main:app --reload
   ```

---

## API Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| POST   | `/users/`     | Create a new user |
| GET    | `/users/{id}` | Get user by ID    |
| PUT    | `/users/{id}` | Update user by ID |
| DELETE | `/users/{id}` | Delete user by ID |
| GET    | `/users/`     | List all users    |

---

## Code Explanation

### 1. **main.py**

- Initializes FastAPI app.
- Includes user routes with `/users` prefix.

### 2. **user_route.py**

- Defines API endpoints for user CRUD operations.
- Uses dependency injection for DB session.

### 3. **user_service.py**

- Contains business logic for user operations.
- Calls repository methods for DB actions.

### 4. **user_repository.py**

- Handles direct database operations (CRUD).
- Uses SQLModel's session for queries.

### 5. **user.py (schemas & models)**

- **schemas/user.py**: Pydantic models for request/response validation.
- **models/user.py**: SQLModel ORM model for the User table.

### 6. **db/session.py**

- Manages database session creation and teardown.

---

## Optimization Tips

- Use async endpoints and DB drivers for better performance.
- Optimize queries and use indexes in PostgreSQL.
- Use a production ASGI server (e.g., Uvicorn with multiple workers).
- Implement caching for heavy read endpoints.

---

## Troubleshooting

- **Connection Timeout**: Ensure PostgreSQL is running and credentials are correct.
- **405 Error**: Check HTTP method and endpoint path.
- **Slow Response**: Profile queries and optimize database access.

---

## Author

- [YS]
- [yadavsatale@gmail.com]

---

## License

This project is licensed under the MIT License.# UserCrud Project Documentation
