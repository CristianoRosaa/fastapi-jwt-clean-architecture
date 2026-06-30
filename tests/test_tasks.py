def test_get_tasks_empty(authorized_client):

    response = authorized_client.get("/tasks")

    assert response.status_code == 200

    assert response.json() == []

def test_create_task(authorized_client):

    response = authorized_client.post(

        "/tasks",

        json = {

            "title" : "Estudar FastAPI",
            "description": "Aprender Pytest"

        }

    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Estudar FastAPI"

    assert data["description"] == "Aprender Pytest"

    assert data["completed"] is False

    assert "id" in data

    assert "owner_id" in data

def test_get_tasks(authorized_client):

    authorized_client.post(

        "/tasks",

        json = {

            "title": "Primeira tarefa",

            "description": "Descrição 1"

        }

    )

    response = authorized_client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1

    assert data[0]["title"] == "Primeira tarefa"

    assert data[0]["description"] == "Descrição 1"

    assert data[0]["completed"] is False

def test_get_by_id(authorized_client):

    create_response = authorized_client.post(

        "/tasks",

        json = {

            "title" : "Minha tarefa",

            "description" : "Descrição da tarefa"

        }        

    )

    task = create_response.json()

    task_id = task["id"]

    response = authorized_client.get(f"/tasks/ {task_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id

    assert data["title"] == "Minha tarefa"

    assert data["description"] == "Descrição da tarefa"

    assert data["completed"] is False


def test_update(authorized_client):

    create_response = authorized_client.post(

        "/tasks",

        json = {

            "title": "Título antigo",

            "description": "Descrição antiga"

        }

    )

    task = create_response.json()

    task_id = task["id"]

    response = authorized_client.put(

        f"/tasks/{task_id}",
        
        json = {

            "title": "Título novo",

            "description": "Descrição nova",

            "completed": True

        }

    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id

    assert data["title"] == "Título novo"

    assert data["description"] == "Descrição nova"

    assert data["completed"] is True

    get_response = authorized_client.get(f"/tasks/{task_id}")

    task = get_response.json()

    assert task["title"] == "Título novo"
    assert task["description"] == "Descrição nova"
    assert task["completed"] is True


def test_delete_task(authorized_client):

    create_response = authorized_client.post(

        "/tasks",

        json = {

            "title": "Apagar tarefa",

            "description": "Será removida"

        }

    )

    task = create_response.json()

    task_id = task["id"]

    response = authorized_client.delete(

        f"/tasks/{task_id}"

    )

    assert response.status_code == 200

    response = authorized_client.get(f"/tasks/{task_id}")

    assert response.status_code == 404


def task_get_tasks_without_token(client):

    response = client.get("/tasks")

    assert response.status_code == 401


def test_get_nonexistent_task(authorized_client):

    response = authorized_client.get("/tasks/999")

    assert response.status_code == 404


def test_update_nonexistent_task(authorized_client):

    response = authorized_client.put(

        "/tasks/999",

        json = {

            "title": "Novo",

            "description": "Nova descrição",

            "completed": "True"

        }

    )

    assert response.status_code == 404


def test_delete_nonexistent_task(authorized_client):

    response = authorized_client.delete("/tasks/999")

    assert response.status_code == 404