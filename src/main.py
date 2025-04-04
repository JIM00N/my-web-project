from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from web import explorer, creature
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/statics", StaticFiles(directory="statics"), name='statics')
templates = Jinja2Templates(directory="src/templates")

app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
