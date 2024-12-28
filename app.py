from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
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

    genai.configure(api_key="AIzaSyAriovt4o-xOOLVvX9VVTIlVbDGV7R1zVc")
    model = genai.GenerativeModel("tunedModels/fsdmitclubprompts-at2t7npovo8l")
    response = model.generate_content(message)

    message_text = response.to_dict()['candidates'][0]['content']['parts'][0]['text']

    return {"message": message_text}