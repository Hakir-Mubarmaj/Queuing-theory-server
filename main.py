from flask import Flask, request, jsonify
from flask_cors import CORS
from model_1 import mm1_queue_metrics_1
from model_2 import mm1_n_queue_metrics_2
from model_3 import mms_queue_metrics_3
from model_4 import mmsn_queue_metrics_4

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/model_1', methods=['POST'])
def model_1():
    # Get JSON data from the request
    data = request.get_json()

    # Extract parameters from the JSON data
    lambda_rate = data.get('lambda_rate')
    mu_rate = data.get('mu_rate')
    
    # Validate input
    if lambda_rate is None or mu_rate is None:
        return jsonify({"error": "Invalid input. Please provide 'lambda_rate', 'mu_rate' in the request body."}), 400

    try:
        # Convert parameters to appropriate types
        lambda_rate = float(lambda_rate)
        mu_rate = float(mu_rate)

        # Calculate metrics using the given parameters
        metrics = mm1_queue_metrics_1(lambda_rate, mu_rate)
        return jsonify(metrics)
    except ValueError:
        return jsonify({"error": "Invalid input types. Ensure 'lambda_rate', 'mu_rate' are floats, and 's', 'n' are integers."}), 400

@app.route('/model_2', methods=['POST'])
def model_2():
    # Get JSON data from the request
    data = request.get_json()

    # Extract parameters from the JSON data
    lambda_rate = data.get('lambda_rate')
    mu_rate = data.get('mu_rate')
    n = data.get('n')

    # Validate input
    if lambda_rate is None or mu_rate is None or n is None:
        return jsonify({"error": "Invalid input. Please provide 'lambda_rate', 'mu_rate' and 'n' in the request body."}), 400

    try:
        # Convert parameters to appropriate types
        lambda_rate = float(lambda_rate)
        mu_rate = float(mu_rate)
        n = int(n)

        # Calculate metrics using the given parameters
        metrics = mm1_n_queue_metrics_2(lambda_rate, mu_rate, n)
        return jsonify(metrics)
    except ValueError:
        return jsonify({"error": "Invalid input types. Ensure 'lambda_rate', 'mu_rate' are floats, and 'n' are integers."}), 400

@app.route('/model_3', methods=['POST'])
def model_3():
    # Get JSON data from the request
    data = request.get_json()

    # Extract parameters from the JSON data
    lambda_rate = data.get('lambda_rate')
    mu_rate = data.get('mu_rate')
    s = data.get('s')

    # Validate input
    if lambda_rate is None or mu_rate is None or s is None:
        return jsonify({"error": "Invalid input. Please provide 'lambda_rate', 'mu_rate', 's' in the request body."}), 400

    try:
        # Convert parameters to appropriate types
        lambda_rate = float(lambda_rate)
        mu_rate = float(mu_rate)
        s = int(s)

        # Calculate metrics using the given parameters
        metrics = mms_queue_metrics_3(lambda_rate, mu_rate, s)
        return jsonify(metrics)
    except ValueError:
        return jsonify({"error": "Invalid input types. Ensure 'lambda_rate', 'mu_rate' are floats, and 's' are integers."}), 400

@app.route('/model_4', methods=['POST'])
def model_4():
    # Get JSON data from the request
    data = request.get_json()

    # Extract parameters from the JSON data
    lambda_rate = data.get('lambda_rate')
    mu_rate = data.get('mu_rate')
    s = data.get('s')
    n = data.get('n')

    # Validate input
    if lambda_rate is None or mu_rate is None or s is None or n is None:
        return jsonify({"error": "Invalid input. Please provide 'lambda_rate', 'mu_rate', 's', and 'n' in the request body."}), 400

    try:
        # Convert parameters to appropriate types
        lambda_rate = float(lambda_rate)
        mu_rate = float(mu_rate)
        s = int(s)
        n = int(n)

        # Calculate metrics using the given parameters
        metrics = mmsn_queue_metrics_4(lambda_rate, mu_rate, s, n)
        return jsonify(metrics)
    except ValueError:
        return jsonify({"error": "Invalid input types. Ensure 'lambda_rate', 'mu_rate' are floats, and 's', 'n' are integers."}), 400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)