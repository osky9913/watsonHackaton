from flask import Flask
app = Flask(__name__)




@app.route('/watsonAI')
def chat():
    return "watsonAI"

@app.route('/')
def ping():
    return "Hello world"



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5001)
    