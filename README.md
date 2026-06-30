# 🚀 FastAPI JWT Clean Architecture


![Python](https://img.shields.io/badge/Python-3.14-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green)

![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)

![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange)

![Pytest](https://img.shields.io/badge/Pytest-Tests-yellow)

![Coverage](https://img.shields.io/badge/Coverage-93%25-brightgreen)


A REST API developed with **FastAPI**, following the principles of **Clean Architecture**, using **JWT** for authentication, **SQLAlchemy** for data persistence, **Alembic** for database migrations, and **Pytest** for automated testing.

The goal of this project was to apply backend development best practices used in real-world applications, prioritizing code oragnization, separation of concerns, and maintainability.
---

# 📌 Features

* User registration
* Login with JWT authentication
* Authenticated user profile
* Full task CRUD
* Search tasks by title
* Result pagination
* Customized exception handling
* Logging system
* Database migration with alembic
* Automated tests
* Test coverage exceeding 90%

---

# 🛠 Technologies

* Python 3.14
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)
* Pytest
* Pytest-Cov
* Uvicorn

---

# 🏛 Architecture

The project was organized using a layered architecture to keep the code decoupled and easy to maintain.  

```
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
```

### Project Structure

```
app/
│
├── core/
├── exceptions/
├── handlers/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
│
tests/
│
alembic/
```

Each layer has a specific responsibility:

* **Routers:** receive the HTTP requests.
* **Services:** contain the business logic.
* **Repositories:** handle database access.
* **Models:** represent database tables.
* **Schemas:** validate data input and output.
* **Core:** authentication, dependencies and configurations.

---

# ⚙️ Installation

Clone the project

```bash
git clone <REPOSITORY_URL>
```

Create a virtual environment 

```bash
python -m venv venv
```

Activate the virtual environment 

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file using the `.env.example` file as a base.

Run the migrations

```bash
alembic upgrade head
```

Start the application

```bash
uvicorn app.main:app --reload
```

The documentation will be available at: 

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Run the tests

Run all the tests

```bash
pytest
```
Generate coverage report

```bash
pytest --cov=app --cov-report=term-missing
```

Current project coverage:

**93%**

---

# 📖 Endpoints

## Authentication

* POST /register
* POST /login
* GET /profile

## Tasks

* GET /tasks
* GET /tasks/{id}
* POST /tasks
* PUT /tasks/{id}
* DELETE /tasks/{id}

---

# 🔒 Security

Authentication is performed using JSON Web Token (JWT). 

After logging in, a token is generated and must be sent in the header of protected requests using the scheme: 

```
Authorization: Bearer <token>
```

---

# 📚 Key Takeaways

During the development of this project, important backend development concepts were applied, including:

* Clean Architecture
* Dependency Injection
* Repository Pattern
* Service Layer
* JWT authentication
* Alembic migrations
* Automated tests
* Test coverage
* Layered organization
* Exception handling
* Logging

---

# 🚀 Future improvements

* Docker and Docker Compose
* Refresh Token
* Rate Limiting
* Cache with Redis
* CI/CD using GitHub Actions
* Cloud Deploy

---

# 👨‍💻 author

# 👨‍💻 Author

Developed by **Cristiano Rosa**.

This project was created as part of my backend development journey, focusing on building production-ready APIs using FastAPI and modern Python technologies.