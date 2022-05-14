from flask import Flask, jsonify, render_template

app = Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/json")
def json_response():
    response = {"type": "dog", "age": 30}
    return jsonify([response])

if __name__ == "__main__":
    app.run(debug=True)