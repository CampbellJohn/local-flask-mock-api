# Quick Local Flask API

This project is a simple Flask application that provides a local API with multiple endpoints.

## Project Structure

```
local-flask-api-app
├── app
│   ├── __init__.py
│   └── routes.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application, execute the following command:

```
python run.py
```

The application will start on `http://127.0.0.1:5000/`.