from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run-pipeline', methods=['POST'])
def run_pipeline():
    return jsonify({"status": "Pipeline executed successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
