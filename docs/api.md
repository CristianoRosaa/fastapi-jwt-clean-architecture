# API Endpoints

Authentication

POST /register

Registers a new user.

POST /login

Authenticates a user and returns a JWT token.

GET /profile

Returns authenticated user information.

---

Tasks

GET /tasks

Returns authenticated user's tasks.

GET /tasks/{id}

Returns a task by id.

POST /tasks

Creates a new task.

PUT /tasks/{id}

Updates a task.

DELETE /tasks/{id}

Deletes a task.