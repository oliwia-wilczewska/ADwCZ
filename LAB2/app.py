from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello', methods=['GET'])
def name():
    name = request.args.get("name", "")
    if name:
        odp = f"Hello {name}!" 
    else:
        odp = f"Hello!"
    return jsonify({"message": odp})

if __name__ == '__main__':
    app.run()
