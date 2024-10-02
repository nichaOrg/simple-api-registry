from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


@app.route("/getcode", methods=["GET"])
def getcode():
    return "getcode"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = f"{num1} + {num2} = {num1 + num2}"
    except:
        results = {"error_msg": "inputs must be numbers"}

    return results

@app.route("/is_prime/<num>", methods=["GET"])
def prime(num):
    num = int(num)
    if num < 2:
        return "false"
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return "false"
    
    return "true"

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    name = str(name)
    return "Hello " + name

@app.route("/minus/<num1>/<num2>", methods=["GET"])
def minus(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = str(num1 - num2)
    except:
        result = {"error_msg": "inputs must be numbers eiei"}

    return result

@app.route("/avg/<num1>/<num2>",methods=["GET"])
def avg(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result=str((num1+num2)/2)
    except:
        result = {"error_msg": "inputs must be numbers eiei"}
    return result

@app.route("/power/<num1>/<num2>",methods=["GET"])
def power(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result=str(pow(num1,num2))
    except:
        result = {"error_msg": "inputs must be numbers eiei"}
    return result

@app.route("/multiply/<num1>/<num2>",methods=["GET"])
def multiply(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result=str(num1*num2)
    except:
        result = {"error_msg": "inputs must be numbers eiei"}
    return result

@app.route("/divide/<num1>/<num2>",methods=["GET"])
def devide(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        # result=str(int(num1/num2)) ไม่มีทศนิยม
        result = "{:.3f}".format(num1 / num2)
    except:
        result = {"error_msg": "inputs must be numbers eiei"}
    return result

@app.route("/mul5/<num1>",methods=["GET"])
def mul5(num1):
    def is_integer(num):
        return float(num1) % 1 == 0
    try:
        num1 = float(num1)
        if (is_integer(num1)):
            result = str(int(num1)*5)
        else:
            result = str(float(num1)*5)

    except:
        result = {"error_msg": "inputs must be numbers eiei"}
    return result

@app.route("/mod/<num1>/<num2>",methods=["GET"])
def mod(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result=str(num1%num2)
    except:
        result = {"error_msg": "inputs must be numbers eiei"}
    return result

@app.route("/More1000/<num1>",methods=["GET"])
def isMoreThan1000(num1):
    try:
        num1 = int(num1)
        if num1 > 1000 :
            result = "this result is False"
        else :
            result = "this result is True"
        
    except:
        result = {"error_msg": "inputs must be numbers eiei"+num1}
    return result


# if __name__ == "__main__":
#     app.run()
