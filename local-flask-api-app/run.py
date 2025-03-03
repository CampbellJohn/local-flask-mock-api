from flask import Flask
from app.routes import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == '__main__':
    # Run the app in debug mode in case extra info's needed.
    app.run(debug=True)