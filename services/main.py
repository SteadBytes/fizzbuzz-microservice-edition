from flask import Flask
import requests

app = Flask(__name__)


@app.route("/<int:n>")
def fizzbuzz(n):
    return "".join(
        r.text.strip()
        for r in (
            requests.get(f"http://{host}:5000/{n}")
            for host in ["fizz", "buzz", "number"]
        )
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
