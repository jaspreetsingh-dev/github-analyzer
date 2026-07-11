from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from github_client import (
    get_user_profile,
    get_repositories
)

from analyzer import (
    calculate_codex_score,
    calculate_basic_stats
)

from summarizer import (
    generate_summary,
    generate_badges
)

from storage import upload_report

import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():

    return send_from_directory(
        "../frontend",
        "index.html"
    )


@app.route("/frontend/<path:filename>")
def frontend_files(filename):

    return send_from_directory(
        "../frontend",
        filename
    )


def build_user_analysis(username):

    profile = get_user_profile(username)

    if profile.get("message") == "API rate limit exceeded":

        return {
            "error": "GitHub API rate limit exceeded. Try again later."
        }, 429

    if profile.get("message") == "Not Found":

        return {
            "error": "Username not found"
        }, 404

    logging.info(f"Analyzing: {username}")

    repos = get_repositories(username)

    stats = calculate_basic_stats(repos)

    codex_score = calculate_codex_score(
        profile,
        repos
    )

    summary = generate_summary(
        profile,
        repos,
        stats,
        codex_score
    )

    badges = generate_badges(
        profile,
        stats
    )

    return {
        "profile": profile,
        "stats": stats,
        "codex_score": codex_score,
        "summary": summary,
        "badges": badges
    }, 200


@app.route("/compare/<username1>/<username2>")
def compare_users(username1, username2):

    try:

        if username1.lower() == username2.lower():

            return jsonify({
                "error": "Please enter two different usernames"
            }), 400

        user1_data, status1 = build_user_analysis(username1)

        if status1 != 200:

            return jsonify(user1_data), status1

        user2_data, status2 = build_user_analysis(username2)

        if status2 != 200:

            return jsonify(user2_data), status2

        comparison_report = {
            "user1": user1_data,
            "user2": user2_data,
            "winner": (
                username1
                if user1_data["codex_score"] >
                user2_data["codex_score"]
                else username2
            )
        }
        upload_report(comparison_report, username1, username2)
        return jsonify(comparison_report)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(debug=True)