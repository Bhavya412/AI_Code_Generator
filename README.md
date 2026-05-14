# AI Code Generator

An AI-powered web application that generates high-quality code using the Groq LLM API.  
Built with Flask, SQLAlchemy, and a modern dark UI.

---

##  Features

-  AI code generation using Groq API (LLaMA 3)
-  Supports multiple languages (Python, Java, C, C++, JavaScript)
-  Prompt-based code generation
-  History storage using SQLite database
-  One-click copy code feature
-  Modern dark UI (minimal design)
-  Fast Flask backend

---

##  Tech Stack

- Python
- Flask
- SQLAlchemy
- HTML / CSS / JavaScript
- Bootstrap
- Groq API (LLaMA 3)

---

##  Project Structure
Ai_Code_Generator/
│── app.py
│── requirements.txt
│── models/
│ └── history_model.py
│── templates/
│ └── index.html
│── static/
│ ├── style.css
│ └── script.js
│── instance/ (ignored)
│── .env (ignored)

## Installation & Setup
1. Clone the repository

git clone https://github.com/your-username/AI_Code_Generator.git
cd AI_Code_Generator

2. Create virtual environment
python -m venv venv

3. Activate virtual environment
Windows:
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Add environment variables
Create a .env file in the root folder:
GROQ_API_KEY=your_api_key_here

6. Run the application
python app.py

🌐 App will run at:
http://127.0.0.1:5000
