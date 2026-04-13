from flask import Flask, jsonify, request
from flask_cors import CORS
from github_client import get_user_profile, get_repositories
from analyzer import calculate_codex_score, calculate_basic_stats
from sumarizer import generate_summary

app = Flask(__name__)
CORS(app)

@app.route("/analyze/<username>")
def analyze_username(username):
    profile = get_user_profile(username)
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

if __name__ == "__main__":
    app.run(debug=True)
    