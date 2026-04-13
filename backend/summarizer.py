def generate_summary(profile, repos, stats, codex_score):
    name = profile["login"]
    top_language = max(stats["languages"], key=stats["languages"].get)
    total_repos = len(repos)

    return f"{name} is a developer with {total_repos} public repositories, primarily working in {top_language}. their Codex Score is ({codex_score}/100)"
