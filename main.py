from fastapi import FastAPI, status
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()


@app.get("/", tags=["index"], response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index():
    return FileResponse("index.html")


@app.get("/styles.css", tags=["styles"], status_code=status.HTTP_200_OK)
async def styles():
    return FileResponse("styles.css", media_type="text/css")
