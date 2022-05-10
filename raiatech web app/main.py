from re import L
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


from models.usuario import *


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def main(request: Request):
    return RedirectResponse("/docs")

@app.get("/login")
def main(request: Request):
    return templates.TemplateResponse("login.html",{"request": request})

@app.get("/login/")
def main(request: Request, id_email_usuario: str, senha_usuario: str):
    user = Usuario()
    recupera = user.verifica_login(id_email_usuario,senha_usuario)
    print(id_email_usuario)

    if recupera == True:
        return RedirectResponse("/")
    else:
        return False

    return templates.TemplateResponse("login.html",{"request": request})

@app.get("/usuario")
def get_all_users():
    user = Usuario()
    return user.consulta()

@app.get("/usuario/{id_email_usuario}")
def get_user_by_id(id_email_usuario: str):
    user = Usuario()
    return user.consulta_usuario(id_email_usuario)


@app.post("/usuario")
def set_user(id_email_usuario: str, codigo_tipo_usuario: int, nome_usuario: str, senha_usuario: str):
    user = Usuario()
    user.inserir(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
    return user
@app.post("/romano")
def numero_romano(string_input: str):
    user = Usuario()
    retorno = user.execute_final(string_input)
    romano = user.intToRoman(retorno[len(retorno)-1])
    dict_retorno = {"number": romano,"value":retorno[len(retorno)-1]}
    return dict_retorno

@app.put("/usuario/{id_email_usuario}")
def put_user(id_email_usuario: str, codigo_tipo_usuario: int, nome_usuario: str, senha_usuario: str):
    user = Usuario()
    user.alterar(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
    return user


@app.delete("/usuario/{id_email_usuario}")
def delete_user(id_email_usuario: str):
    user = Usuario()
    user.excluir(id_email_usuario)
    return "Ok"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
