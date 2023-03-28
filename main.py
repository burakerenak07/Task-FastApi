from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from extract import *
import os
from fastapi import FastAPI, Form, Request



SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


app = FastAPI()
inventory={}


@app.post("/process_link")
async def process_link(link: str = Form(...)):
    exec=getIt(link)
    inventory[0]=exec
    return inventory[0]

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return """
        <html>
            <head>
                <title>Get link and process</title>
            </head>
            <body>
                <form method="post" action="/process_link">
                    <input type="text" name="link">
                    <button type="submit">Process link</button>
                </form>
            </body>
        </html>
    """
 