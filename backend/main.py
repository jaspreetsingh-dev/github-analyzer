from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from github_client import get_user_profile, get_repositories
from analyzer import calculate_codex_score, calculate_basic_stats
from summarizer import generate_summary

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/analyze/<username>")
def analyze_username(username):
    try:
        profile = get_user_profile(username)

        if "message" in profile:
            return jsonify({"error": "Username not found"}), 404
        
        repos = get_repositories(username)
        stats = calculate_basic_stats(repos)
        codex_score = calculate_codex_score(profile, repos)
        summary = generate_summary(profile, repos, stats, codex_score)

        return jsonify({
            "profile": profile,
            "stats": stats,
            "codex_score": codex_score,
            "summary": summary
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
    