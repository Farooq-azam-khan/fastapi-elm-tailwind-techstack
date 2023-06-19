from fastapi import FastAPI

from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel,  validator
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8000",
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/assets', StaticFiles(directory='./assets'), name='asset_files')
templates = Jinja2Templates(directory='templates')

api = APIRouter(
    prefix='/api', tags=['api'], responses={404: {'description': 'api route not found...'}})


class User(BaseModel):
    email: str
    username: str

    @validator('email')
    def validate_email(cls, v):
        if len(v) <= 0:
            raise ValueError('Email is a required field')
        elif '@' not in v or '.' not in v:
            raise ValueError('Invalid Email value')
        return v


@api.post('/user')
def get_user(user: User):
    print(user)
    return []


app.include_router(api)


@app.get('/')
def home():
    return {'Hello': 'World'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
