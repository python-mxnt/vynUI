from flask import Flask, render_template, request

vynUI = Flask(__name__)

@vynUI.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@vynUI.route('/post', methods=['POST'])
def post():
    return "recived: {}".format(request.form)

if __name__ == "__main__":
    vynUI.run(debug=True)