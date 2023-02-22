# main.py

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations, it's a web app!"


@app.route("/<celsius_to_convert>")
def fahrenheit_from(celsius_to_convert):
    """Convert celsius to fahrenheit degrees."""
    try:
        fahrenheit = float(celsius_to_convert) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return f"Invalid input"


if __name__ == "__main__":
    celsius = input("Celsius: ")
    print(f"Fahrenheit: {fahrenheit_from(celsius)}")


# This two lines tells Python to start Flask's development server.
# when the script is executed from the command line.

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
