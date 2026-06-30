# Architecture

This project follows a layered architecture inspired by Clean Architecture principles.

Request Flow

Client
   │
   ▼
Routers
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
Database

Responsibilities

- Routers
  Handle HTTP requests and responses.

- Services
  Contain business logic.

- Repositories
  Encapsulate database operations.

- Models
  SQLAlchemy ORM models.

- Schemas
  Pydantic models for validation.

- Core
  Authentication, security, dependencies and configuration.

Benefits

- Separation of concerns
- Easier maintenance
- Better scalability
- Easier testing