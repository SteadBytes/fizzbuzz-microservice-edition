from flask import Flask

app = Flask(__name__)


@app.route("/<int:n>")
def buzz(n):
    return "Buzz" if n % 5 == 0 else ("", 200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
