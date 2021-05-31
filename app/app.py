import os
import subprocess
from ork.namegen import NameGenerator
from flask import Flask, request

# Flask
app = Flask(__name__)


@app.route('/name', methods=['GET', 'OPTIONS'])
def name():
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '86400'  # firefox max
        }
        return '', 204, headers

    headers = {
        'Access-Control-Allow-Origin': "*",
        'Content-Type': "application/json"
    }
    query_args = request.args
    generated_name = NameGenerator.generate(faction_name=query_args.get("faction_name"), lang=query_args.get("lang"))
    return {"name": generated_name}, 200, headers




# dev
if __name__ == "__main__":
    # curl -G http://127.0.0.1:5000/name --data-urlencode 'faction_name=orks' --data-urlencode 'lang=fr'
    os.environ["FLASK_APP"] = "app.py"
    subprocess.call(["python3", "-m", "flask", "run"])
