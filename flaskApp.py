from flask import Flask, jsonify, request

app = Flask(__name__)

contacts =[
     {
          "Contact": "9999994733",
          "Name": "Niall",
          "done": False,
          "id": 1
     },
     {
          "Contact": "9853394731",
          "Name": "Liam",
          "done": False,
          "id": 1
     },
     {
          "Contact": "7849026388",
          "Name": "Zayn",
          "done": False,
          "id": 3
     }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    task = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
        