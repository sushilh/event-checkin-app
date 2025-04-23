from flask import Flask, request, jsonify, send_from_directory
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CSV_FILE = 'attendees.csv'

def read_csv():
    with open(CSV_FILE, newline='') as f:
        return list(csv.DictReader(f))

def write_csv(data):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "attendees", "allergy", "checked_in"])
        writer.writeheader()
        writer.writerows(data)

@app.route('/attendees', methods=['GET'])
def get_attendees():
    return jsonify(read_csv())

@app.route('/checkin', methods=['POST'])
def check_in():
    email = request.json.get('email')
    data = read_csv()
    for row in data:
        if row['email'] == email:
            row['checked_in'] = 'yes'
            break
    write_csv(data)
    return jsonify({"status": "success", "email": email})

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)