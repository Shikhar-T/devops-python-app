from flask import Flask
app = Flask(__name__)

@app.route('/')
def combined_message():
    line1 = "Hello DevOps 🚀"
    line2 = "Hello FINAL CI/CD Namaste 🚀 🚀"
    return f"{line1} <br> {line2}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
