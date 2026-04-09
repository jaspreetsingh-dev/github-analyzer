
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
