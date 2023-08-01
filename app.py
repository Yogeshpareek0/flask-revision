from flask import Flask , request , render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to flask'
@app.route('/htmlfile')


app.run()