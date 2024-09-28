from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World ได้สักที่ไหว้สาธุเลย"


@app.route("/getcode", methods=["GET"])
def getcode():
    return "getcode test2"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = f"{num1} + {num2} = {num1 + num2}"
    except:
        results = {"error_msg": "inputs must be numbers"}

    return results


if __name__ == "__main__":
    app.run()
