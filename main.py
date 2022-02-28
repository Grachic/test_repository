from fastapi import FastAPI, Body
import uvicorn
from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get('/')
def start_window():
    s = 'Чё-то на странице'
    return PlainTextResponse(s)


uvicorn.run(app)
