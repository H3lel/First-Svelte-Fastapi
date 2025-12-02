from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

app = FastAPI()

build_dir = Path(__file__).parent.parent / "frontend" / "build"










# 1️⃣ Serve SvelteKit static folders
app.mount("/_app", StaticFiles(directory=build_dir / "_app"), name="_app")

app.mount("/immutable", StaticFiles(directory=build_dir / "_app" / "immutable"), name="immutable")


# 3️⃣ Fallback to index.html for all other routes (SPA routing)
@app.get("/{full_path:path}")
async def spa_fallback(full_path: str):
    return FileResponse(build_dir / "index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
