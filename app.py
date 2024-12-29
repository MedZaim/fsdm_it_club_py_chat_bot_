import os

import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Load environment variables from .env file
load_dotenv()

# Read API Key and model name from environment variables
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/chatbot")
async def say_hello(request: Request):
    data = await request.json()
    message = data.get("message")


    #Configure API key   &   Use model name from environment variables
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)

    response = model.generate_content(message)

    message_text = response.to_dict()['candidates'][0]['content']['parts'][0]['text']

    return {"message": message_text}