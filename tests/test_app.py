import pytest
from app import create_app

@pytest.fixture()
def client(tmp_path):
    database = tmp_path / "test.db"
    app = create_app({"TESTING": True, "DATABASE": str(database), "SECRET_KEY": "test"})
    with app.test_client() as client:
        yield client

def test_home_page_displays_title(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Gerenciamento de tarefas" in response.data

def test_create_task(client):
    response = client.post("/tasks", data={"title": "Preparar entrega", "description": "Finalizar projeto"})
    assert response.status_code == 302
    page = client.get("/")
    assert b"Preparar entrega" in page.data

def test_task_requires_title(client):
    client.post("/tasks", data={"title": "   "})
    page = client.get("/")
    assert "O título da tarefa é obrigatório.".encode() in page.data

def test_update_task_status(client):
    client.post("/tasks", data={"title": "Testar sistema"})
    client.post("/tasks/1/status", data={"status": "Concluído"})
    page = client.get("/")
    assert b"Conclu" in page.data

def test_delete_task(client):
    client.post("/tasks", data={"title": "Excluir depois"})
    client.post("/tasks/1/delete")
    page = client.get("/")
    assert b"Excluir depois" not in page.data

def test_new_task_starts_with_pending_status(client):
    client.post("/tasks", data={"title": "Nova atividade"})
    page = client.get("/")
    assert b"A Fazer" in page.data


def test_invalid_status_is_rejected(client):
    client.post("/tasks", data={"title": "Testar status"})
    response = client.post(
        "/tasks/1/status",
        data={"status": "Status Inválido"}
    )
    assert response.status_code == 302
    page = client.get("/")
    assert b"Status inv" in page.data


def test_task_description_is_saved(client):
    client.post(
        "/tasks",
        data={
            "title": "Documentação",
            "description": "Criar documentação do sistema"
        }
    )
    page = client.get("/")
    assert b"Criar documenta" in page.data
