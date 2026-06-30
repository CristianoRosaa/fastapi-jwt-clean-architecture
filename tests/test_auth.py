def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {

        "message": "Project clean and working"

    }


def test_register(client):

    response = client.post(

        "/register",
        json = {

            "username": "cristiano",
            "email": "cristiano@email.com",
            "password": "123456"

        }

    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "cristiano"

    assert data["email"] == "cristiano@email.com"

    assert "password" not in data

def test_login(client):

    client.post(

        "/register",

        json = {

            "username": "lucas",

            "email":  "lucas@email.com",

            "password": "123456"        

        }

    )

    response = client.post(

        "/login",

        data = {

            "username": "lucas",
            "password": "123456"

        }

    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data

    assert data["token_type"] == "bearer"


def test_login_invalid_password(client):

    client.post(

        "/register",

        json = {

            "username": "lucas",

            "email": "lucas@email.com",

            "password": "123456"

        }


    )

    response = client.post(

        "/login",

        data = {

            "username": "lucas",

            "password": "senha_errada"

        }

    )

    assert response.status_code == 401

    assert response.json()["detail"] == "Invalid Credentials"


def test_register_duplicate_username(client):

    user = {

        "username": "lucas",

        "email": "lucas@email.com",

        "password": "123456"

    }

    client.post("/register", json = user)

    response = client.post("/register", json = user)

    assert response.status_code == 400


def test_register_duplicate_email(client):

    client.post(

        "/register",

        json = {

            "username": "lucas",

            "email": "lucas@email.com",

            "password": "123456"

        }

    )


    response = client.post(

        "/register",

        json = {

            "username": "pedro",

            "email": "lucas@email.com",

            "password": "654321"

        }

    )

    assert response.status_code == 400
