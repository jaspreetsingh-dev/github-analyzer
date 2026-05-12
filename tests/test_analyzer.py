import sys
sys.path.append("backend")

from analyzer import calculate_basic_stats
from analyzer import calculate_codex_score
from summarizer import get_star_tier, get_account_age, generate_summary, generate_badges


def test_basic_stats():
    fake_repos = [
        {"stargazers_count": 10, "forks_count": 5, "language": "Python", "description": "test"},
        {"stargazers_count": 20, "forks_count": 3, "language": "JavaScript", "description": ""},
        {"stargazers_count": 5, "forks_count": 1, "language": None, "description": "test"}
    ]

    result = calculate_basic_stats(fake_repos)

    assert result["total_stars"] == 35
    assert result["total_forks"] == 9
    assert "Python" in result["languages"]
    assert None not in result["languages"]

    print("All tests passed for basic stats")


def test_codex_score_empty_repos():
    fake_profile = {"followers": 444}
    result = calculate_codex_score(fake_profile, [])
    assert result == 0

    print("All tests passed for codex score")


def test_get_star_tier():
    assert get_star_tier(0) == "emerging developer"
    assert get_star_tier(50000) == "top 1% on Github"
    assert get_star_tier(500) == "recognised developer"

    print("All tests passed star tier")


def test_get_account_age():
    assert get_account_age("2010-01-01T00:00:00Z") == "veteran of the community"
    assert get_account_age("2024-01-01T00:00:00Z") == "relatively new to Github"

    print("All tests passed account age")


def test_generate_summary_contains_username():
    fake_profile = {"login": "fakeuser", "followers": 444, "created_at": "2010-01-01T00:00:00Z"}
    fake_stats = {"total_stars": 222, "total_forks": 333, "languages": {"python": 5}}
    fake_codex_score = 75.0
    fake_repos = []

    result = generate_summary(fake_profile, fake_repos, fake_stats, fake_codex_score)
    assert "fakeuser" in result

    print("All tests passed for summary")


def test_generate_badges_star_collector():
    fake_profile = {"created_at": "2010-01-01T00:00:00Z"}
    fake_stats = {"total_stars": 150, "total_forks": 200, "languages": {"python": 2}}
    result = generate_badges(fake_profile, fake_stats)
    assert any("Star Collector" in badge for badge in result)

    print("All tests passed for badges")


if __name__ == "__main__":

    test_basic_stats()
    test_codex_score_empty_repos()
    test_get_star_tier()
    test_get_account_age()
    test_generate_summary_contains_username()
    test_generate_badges_star_collector()