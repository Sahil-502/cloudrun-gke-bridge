import os
import requests
from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the frontend HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Fetch data from the GKE service
@app.route('/fetch')
def fetch_gke_data():
    try:
        # Private GKE service URL (from ENV or fallback to default)
        app_url = os.environ.get("GKE_SERVICE_URL", "http://34.93.184.169:80")
        app.logger.info(f"Fetching data from {app_url}")

        # Use timeout to avoid hanging if backend is slow
        response = requests.get(app_url, timeout=5)
        app.logger.info(f"Response received with status {response.status_code}")

        return response.text

    except requests.exceptions.Timeout:
        app.logger.error("Request to GKE service timed out")
        return "Error: Backend request timed out", 504

    except Exception as e:
        app.logger.error(f"Error while fetching GKE data: {str(e)}")
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
