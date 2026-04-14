def calculate_basic_stats(repos):
    total_stars = 0
    total_forks = 0
    languages = {}
    for repo in repos:
        total_stars += repo["stargazers_count"]
        total_forks += repo["forks_count"]
        language = repo["language"]
        if language is None: continue
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
    return {
        "total_stars": total_stars,
        "total_forks": total_forks,
        "languages": languages
    }

def calculate_codex_score(profile, repos):
    if len(repos) == 0:
        return 0
    total_repos = len(repos)
    total_stars = sum(repo["stargazers_count"] for repo in repos)
    total_forks = sum(repo["forks_count"] for repo in repos if repo["language"])
    followers = profile["followers"]
    languages = set(repo["language"] for repo in repos if repo["language"])
    described = sum(1 for repo in repos if repo["description"])

    star_score = min(total_stars/ 1000 * 100, 100)
    community_score = min((followers + total_forks) / 500 * 100, 100)
    consistency_score = min(total_repos / 30 *100, 100)
    doc_score = (described / total_repos * 100) if total_repos > 0 else 0
    diversity_score = min(len(languages) / 10 * 100, 100)

    codex_score = (
        star_score * 0.25 +
        community_score * 0.20 +
        consistency_score * 0.20 +
        doc_score * 0.20 +
        diversity_score * 0.15 
    )

    return round(codex_score, 2)

