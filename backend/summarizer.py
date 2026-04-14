def generate_summary(profile, repos, stats, codex_score):
    name = profile["login"]
    top_language = max(stats["languages"], key=stats["languages"].get)
    total_repos = len(repos)

    return f"{name} is a developer with {total_repos} public repositories, primarily working in {top_language}. their Codex Score is ({codex_score}/100)"

def generate_badges(profile, stats):
    badges = []
    year = int(profile["created_at"][:4])
    if year < 2015:
        badges.append("🏆 Veteran")
    if stats["total_stars"] > 100:
        badges.append("⭐ Star Collector")
    if len(stats["languages"]) > 3:
        badges.append("🌐 Polyglot")
    top_language =max(stats["languages"], key=stats["languages"].get)
    badges.append("💻 " + top_language)
    return badges
