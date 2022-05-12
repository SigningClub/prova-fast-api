from re import L
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


from models.romano import *


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
romano_principal = romano()
romano_secundário = Solution()
@app.get("/")
def main(request: Request):
    return RedirectResponse("/docs")

@app.post("/search")
def numero_romano(string_input: str):
    retorno = romano_principal.execute_final(string_input)
    romano = romano_secundário.intToRoman(retorno[len(retorno)-1])
    dict_retorno = {"number": romano,"value":retorno[len(retorno)-1]}
    return dict_retorno



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



