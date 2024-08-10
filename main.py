from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.user_routes import user_router

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

app.mount("/assets", StaticFiles(directory="./assets"), name="asset_files")
templates = Jinja2Templates(directory="templates")

app.include_router(user_router)


@app.get("/api/version/latest")
def api_latest_version():
    return "v0.2"


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
