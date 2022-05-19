from turtle import st
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def Raiz():
    return {"Hello": "World"}


# Base modelo 
class Users(BaseModel):
    id: int
    email: str
    password: str

#Criar a Base dados

base_de_dados = [
    Users(id=1, email="kaue@example.com", password="123456"),
    Users(id=2, email="teste@example.com", password="testeteste"),
    Users(id=3, email="kaue221@example.com", password="123456eee"),
]

# Rota All

@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota por ID
@app.get("/usuarios/{id}")
def get_usuario_por_id(id_usuario: int):
    for usuario in base_de_dados:
        if (usuario.id == id_usuario):
            return usuario

    return {"Status": "Usuario não encontrado"}

# Rota por EMAIL
@app.get("/usuarios/email/{email}")
def get_usuario_por_email(email_usuario: str):
    for usuario in base_de_dados:
        if (usuario.email == email_usuario):
            return usuario

    return {"Status": 404, "Error":"Usuario não encontrado"}


# Rota para inserir usuario
@app.post("/usuarios")
def inserir_usuario(usuario: Users):
    base_de_dados.append(usuario)
    return usuario

# Rota de deletar usuario

@app.delete("/usuarios/{id}")
def deletar_usuario(id_usuario: int):
    for usuario in base_de_dados:
        if (usuario.id == id_usuario):
            base_de_dados.remove(usuario)
            return {"Status": "Usuario removido com sucesso"}
    return {"Status": "Usuario não encontrado"}

# rota de atualizar usuario
@app.put("/usuarios/{id}")
async def atualizar_usuario(id_usuario: int, usuario: Users):
    atualizar_usuario = get_usuario_por_id(id_usuario)
    if atualizar_usuario:
        atualizar_usuario.email = usuario.email
        atualizar_usuario.password = usuario.password
        return atualizar_usuario