from flask import Flask , request , render_template,jsonify
import json

app = Flask(__name__)

@app.route('/',methods = ["GET"])
def welcome():
    return 'welcome to flask'

@app.route('/printData',methods = ["POST"])
def printval():
    val1 = request.json["val1"]
    return val1

# @app.route('/calculator',methods = ["GET"])
# def matfunc():
#     operation = request.json["operation"]
#     number1 = request.json["number1"]
#     number2 = request.json["number2"]
#     if operation == "add":
#         result = int(number1)+int(number2)
#     elif operation == "div":
#         result = int(number1)/int(number2)
#     elif operation == "multi":
#         result = int(number1)*int(number2)
#     else:
#         result = int(number1)-int(number2)

#     return jsonify(result)


if __name__=="__main__":

    app.run(debug=True)