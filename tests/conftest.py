import os

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABSE_URL = "sqlite:///./test.db"

engine = create_engine(

    SQLALCHEMY_DATABSE_URL,
    connect_args={"check_same_thread": False}

)

TestingSessionLocal = sessionmaker(

    autocommit = False,
    autoflush = False,
    bind = engine 

)

@pytest.fixture

def db():

    Base.metadata.create_all(bind=engine)

    database = TestingSessionLocal()

    try:

        yield database

    finally:

        database.close()

        Base.metadata.drop_all(bind=engine)


def override_get_db():

    database = TestingSessionLocal()

    try:

        yield database

    finally: 

        database.close()

@pytest.fixture

def client(db):

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:

        yield client

    app.dependency_overrides.clear()

@pytest.fixture

def user(client):

    response = client.post(

        "/register",

        json = {

            "username": "teste",
            "email": "teste@email.com",
            "password": "123456"

        }

    )


    return response.json()

@pytest.fixture

def token(client, user):

    response = client.post(

        "/login",

        data = {

            "username": "teste",

            "password": "123456"

        }

    )

    return response.json()["access_token"]

@pytest.fixture

def authorized_client(client, token):

    client.headers = {

        "Authorization": f"Bearer {token}"

    }

    return client

