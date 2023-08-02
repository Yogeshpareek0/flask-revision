from flask import Flask , request , render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to flask'

@app.route('/printData',methods = ["POST"])
def printval():
    
    operation = request.json["operation"]
    val1 = request.json["val1"]
    val2 = request.json["val2"]
    if operation=="multi":
        result = val1*val2
    return str(f'the operation is {operation} and the result is {result}')

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