# 🤖 AI Monitor Sales Assistant (Web)

AI-powered sales assistant for monitor selection and order processing.

The project simulates an online store consultant that helps customers choose a monitor, collects order information, confirms purchases, and automatically stores completed orders in Google Sheets.

---

# ✨ Features

### 💬 AI-powered consultation

* Product recommendations based on customer needs
* Budget clarification
* Gaming, office and design scenarios
* Multi-step conversation flow
* Context-aware responses

### 🛒 Order processing

* Collects customer information
* Confirms order details
* Detects completed orders
* Automatically stores completed orders

### 📊 Google Sheets integration

* Automatic order logging
* Shared order database
* Source tracking

### 🎨 Web interface

* Flask-powered website
* Dark neon-themed UI
* Embedded chat widget
* Session-based conversation history

---

# 🏗 System Architecture

```text
Customer
    │
    ▼
Flask Website
    │
    ▼
OpenAI API
    │
    ▼
Order Extraction
    │
    ▼
Google Sheets
```

---

# 🔗 Related Projects

This repository is part of a larger AI assistant ecosystem.

The same Google Sheets database is shared with the Telegram version of the assistant.

```text
Telegram AI Assistant ──┐
                        │
                        ▼
                  Google Sheets
                        ▲
                        │
Flask Web Assistant ────┘
```

The `source` column is used to identify where each order originated.

| Source   | Description           |
| -------- | --------------------- |
| website  | Flask Web Application |
| telegram | Telegram AI Assistant |

Related repository:

* telegram-ai-assistant *[(here!)](https://github.com/VikkMoor/telegram-ai-assistant)*

---

# 🛠 Tech Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Backend                   |
| Flask             | Web Framework             |
| OpenAI API        | AI Assistant              |
| Google Sheets API | Data Storage              |
| gspread           | Google Sheets Integration |
| HTML              | Frontend                  |
| CSS               | Styling                   |
| JavaScript        | Chat Logic                |

---

# 📁 Project Structure

```text
ai_chat_website/
│
├── main.py
├── ai_logic.py
├── sheets.py
├── config.py
├── requirements.txt
├── .env
├── credentials.json
│
├── templates/
│   └── index.html
│
└── static/
    ├── styles.css
    └── chat.js
```

---

# ⚙️ Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4o-mini

GOOGLE_SHEET_ID=your_sheet_id
GOOGLE_SHEET_WORKSHEET=Sheet1

GOOGLE_CREDENTIALS_PATH=credentials.json

FLASK_SECRET_KEY=your_secret_key

HOST=127.0.0.1
PORT=5000
DEBUG=True
```

---

# 🚀 Installation

### Clone repository

```bash
git clone <repository-url>
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run application

```bash
python main.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 📋 Order Workflow

```text
Customer enters chat
        │
        ▼
AI identifies requirements
        │
        ▼
Monitor recommendation
        │
        ▼
Order data collection
        │
        ▼
Order confirmation
        │
        ▼
Google Sheets storage
```

---

# 📊 Stored Order Format

Orders are stored in Google Sheets using the following structure:

```text
created_at
name
contact
model
quantity
address
payment
telegram_id
source
```

Example:

```text
2026-06-09 18:10:45
John Doe
+123456789
LG UltraGear 27GP850
1
Berlin
Card
123456789
website
```

---

# 🔮 Future Improvements

* VPS deployment
* CRM integration
* Analytics dashboard
* Admin panel
* Product catalog management
* Authentication system

---

# 👩‍💻 Learning Goals

This project was created to practice:

* Flask development
* OpenAI API integration
* Session management
* Google Sheets automation
* AI-powered sales workflows
* Git and GitHub workflows
