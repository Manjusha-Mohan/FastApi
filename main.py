from fastapi import FastAPI,Request
from db import models
from db.database import engine
from router import user,file
from db import models
from schemas import UserBase, UserDisplay
from fastapi.staticfiles import StaticFiles
import os




app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")

app.include_router(user.router)
app.include_router(file.router)

@app.get("/")
def index():
    return {"Hello":"World"}
    


@app.get("/images")
def images():
    out = []
    for filename in os.listdir("files"):
        out.append({
            "name": filename.split(".")[0],
            "path": "files" + filename
        })
    return out


models.Base.metadata.create_all(engine)