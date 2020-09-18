import models

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine

from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    """
    Displays the stock screener dashboard
    """
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
        },
    )


@app.post("/stock")
def create_stock():
    """
    create_stock - Creates a stock and stores it in the database
    """
    return {"status": "code_created"}
