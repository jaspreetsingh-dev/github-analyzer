from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from github_client import get_user_profile, get_repositories
from analyzer import calculate_codex_score, calculate_basic_stats
from summarizer import generate_summary, generate_badges

import logging
logging.basicConfig(level=logging.INFO)

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
            if profile["message"] == "API rate limit exceeded":
                return jsonify({"error": "GitHub API rate limit exceeded. Try again in an hour."}), 429
            return jsonify({"error": "Username not found"}), 404
        
        logging.info(f"Analyzing: {username}")
        
        repos = get_repositories(username)
        stats = calculate_basic_stats(repos)
        codex_score = calculate_codex_score(profile, repos)
        summary = generate_summary(profile, repos, stats, codex_score)
        badges = generate_badges(profile, stats)

        return jsonify({
            "profile": profile,
            "stats": stats,
            "codex_score": codex_score,
            "summary": summary,
            "badges": badges
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/compare/<username1>/<username2>")
def compare_users(username1, username2):
    try:
        if username1.lower() == username2.lower():
            return jsonify({"error": "Please enter two different usernames"}), 400

        profile = get_user_profile(username1)
        if "message" in profile:
            if profile["message"] == "API rate limit exceeded":
                return jsonify({"error": "GitHub API rate limit exceeded. Try again in an hour."}), 429
            return jsonify({"error": "Username not found"}), 404
        
        repos = get_repositories(username1)
        stats = calculate_basic_stats(repos)
        codex_score = calculate_codex_score(profile, repos)
        summary = generate_summary(profile, repos, stats, codex_score)
        badges = generate_badges(profile, stats)

        profile2 = get_user_profile(username2)
        if "message" in profile2:
            return jsonify({"error": "Username not found"}), 404
        
        repos2 = get_repositories(username2)
        stats2 = calculate_basic_stats(repos2)
        codex_score2 = calculate_codex_score(profile2, repos2)
        summary2 = generate_summary(profile2, repos2, stats2, codex_score2)
        badges2 = generate_badges(profile2, stats2)

        return jsonify({
            "user1": {
                "profile": profile,
                "stats": stats,
                "codex_score": codex_score,
                "summary": summary,
                "badges": badges
            },
            "user2": {
                "profile": profile2,
                "stats": stats2,
                "codex_score": codex_score2,
                "summary": summary2,
                "badges": badges2
            },
            "winner": username1 if codex_score > codex_score2 else username2
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
    