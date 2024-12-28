# Chatbot for FSDM IT Club

This project is a chatbot application developed for the **FSDM IT Club**. It's built using **FastAPI** as the web framework and integrates with **Google Generative AI** to handle text-based responses. The project demonstrates the use of modern AI and web technology to create an interactive and intelligent chatbot for the club's use cases.

## Features

- **Interactive Chat**: Users can send messages to the chatbot and get intelligent AI-generated responses.
- **Fast and Scalable**: Built using FastAPI, known for its speed and scalability.
- **Generative AI Integration**: Leveraging Google Generative AI models for natural language responses.
- **Custom Prompts**: Tailored to suit the needs and preferences of the FSDM IT Club.

---

## Project Setup and Requirements

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- A package manager like `pip`
- API key for Google Generative AI

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MedZaim/fsdm_it_club_py_chat_bot_
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Install all required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**:
   Replace the placeholder API key in the code with your actual API key for Google Generative AI:
   ```plaintext
   genai.configure(api_key="<YOUR_API_KEY>")
   ```

4. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the Application**:
   By default, the application will run on:
   ```
   http://127.0.0.1:8000
   ```

---

## API Endpoints

1. **Home Route** (`GET /`):
    - Returns the HTML page (`index.html`) served via Jinja2 templates.

2. **Chatbot API** (`POST /api/chatbot`):
    - Accepts a JSON payload with the user's message.
    - Returns an AI-generated response based on the input message.

   **Example Request**:
   ```json
   {
       "message": "Hello, chatbot!"
   }
   ```

   **Example Response**:
   ```json
   {
       "message": "Hello! How can I assist you today?"
   }
   ```

---

## Project Structure
```
.            
├── main.py            
├── templates/             
│      └── index.html    
├── requirements.txt  
└── README.md    
```
---

## How It Works

1. Users interact with the chatbot through the frontend or via API requests.
2. The chatbot processes the input message and sends it to the Google Generative AI model.
3. The AI model generates a response that is sent back to the user.

---

## Future Improvements


- Implement user authentication for more personalized interactions.
- Deploy on a cloud provider for broader accessibility.

---

## How to Contribute

We welcome contributions to improve and expand the functionality of this chatbot!

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Open a pull request.

---



For any questions or feedback, feel free to contact the FSDM IT Club! 😊