from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path
import uvicorn


build_dir = Path(__file__).parent.parent / "frontend" / "build"
#static_dir = os.path.join( Path.cwd().parent ,"frontend/" ) 

app = FastAPI()

app.mount("/", StaticFiles(directory=str(build_dir), html=True), name="static")


@app.get("/")
def index():
    return FileResponse("build/index.html")

@app.get("/1")
def index():
    return {"test1"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")