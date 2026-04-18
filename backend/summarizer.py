def get_star_tier(total_stars):
    if total_stars == 0:
        return "emerging developer"
    elif total_stars < 100:
        return "growing presence"
    elif total_stars < 1000:
        return "recognised developer"
    elif total_stars < 10000:
        return "well established"
    else:
        return "top 1% on Github"
    
def get_account_age(created_at):
    age = 2026 - int(created_at[:4])
    if age < 2:
        return "relatively new to Github"
    elif age < 5:
        return "experienced developer"
    else:
        return "veteran of the community" 



def generate_summary(profile, repos, stats, codex_score):
    name = profile["login"]
    top_language = max(stats["languages"], key=stats["languages"].get)
    total_repos = len(repos)
    tier = get_star_tier(stats["total_stars"])
    age_label = get_account_age(profile["created_at"])

    return f"{name} is a {tier} and a {age_label} with {total_repos} public repositories, primarily working in {top_language}. their Codex Score is ({codex_score}/100)"

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
