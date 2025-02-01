from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample in-memory data store to hold application data
applications = {}
application_counter = 1

# Possible statuses
STATUS_LIST = ["not found", "received", "processing", "accepted", "rejected"]

@app.route('/')
def index():
    return render_template('index.html')

# Accept new application
@app.route('/apply', methods=['POST'])
def accept_application():
    global application_counter
    name = request.form.get('name')
    zipcode = request.form.get('zipcode')

    if not name or not zipcode:
        return jsonify({"error": "Name and Zipcode are required."}), 400

    application_number = application_counter
    applications[application_number] = {"name": name, "zipcode": zipcode, "status": "received"}
    application_counter += 1

    return jsonify({"application_number": application_number})

# Check application status
@app.route('/status/<int:application_number>', methods=['GET'])
def check_status(application_number):
    application = applications.get(application_number)
    if not application:
        return jsonify({"status": "not found"})
    return jsonify({"status": application['status']})

# Change application status
@app.route('/update_status', methods=['POST'])
def update_status():
    application_number = int(request.form.get('application_number'))
    new_status = request.form.get('status')

    if application_number not in applications:
        return jsonify({"error": "Application not found."}), 404

    if new_status not in STATUS_LIST[1:]:  # Skip "not found" in allowed updates
        return jsonify({"error": f"Invalid status. Allowed values are: {', '.join(STATUS_LIST[1:])}"}), 400

    applications[application_number]['status'] = new_status
    return jsonify({"message": "Status updated successfully."})

if __name__ == '__main__':
    app.run(debug=True)
