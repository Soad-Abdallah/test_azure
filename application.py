from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/")
def hello():
    return "heysss"
if __name__ == '__main__':
    #app.run(threaded=False)
    app.run(debug=True)        