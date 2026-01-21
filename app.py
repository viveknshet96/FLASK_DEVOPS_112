from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask CI/CD Pipeline with Docker Swarm ____vivek___MAHAGANAPATHI"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
