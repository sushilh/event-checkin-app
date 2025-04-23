from flask import Flask, request, jsonify, send_from_directory
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CSV_FILE = 'attendees.csv'
FIELDNAMES = ['name', 'email', 'attendees', 'allergy', 'checked_in']

def read_csv():
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def write_csv(data):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)

@app.route('/attendees', methods=['GET'])
def get_attendees():
    return jsonify(read_csv())

@app.route('/checkin', methods=['POST'])
def toggle_checkin():
    body = request.json
    email = body.get('email')
    new_state = body.get('checked_in')  # "yes" or "no"
    data = read_csv()
    for row in data:
        if row['email'] == email:
            row['checked_in'] = new_state
            break
    write_csv(data)
    return jsonify({"status": "success", "email": email, "checked_in": new_state})

@app.route('/attendees', methods=['PUT'])
def update_attendee_count():
    body = request.json
    email = body.get('email')
    attendees = body.get('attendees', 0)
    data = read_csv()
    for row in data:
        if row['email'] == email:
            row['attendees'] = str(attendees)
            break
    write_csv(data)
    return jsonify({"status": "updated", "email": email, "attendees": attendees})

@app.route('/add', methods=['POST'])
def add_guest():
    new_guest = request.json
    data = read_csv()
    data.append(new_guest)
    write_csv(data)
    return jsonify({"status": "added"})

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)