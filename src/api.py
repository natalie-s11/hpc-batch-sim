from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "jobs_dir": os.path.exists("outputs")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

