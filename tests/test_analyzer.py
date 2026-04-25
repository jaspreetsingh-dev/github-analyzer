import sys
sys.path.append("backend")

from analyzer import calculate_basic_stats

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

    print("All tests passed")

test_basic_stats()

from analyzer import calculate_codex_score

def test_codex_score_empty_repos():
    fake_profile = {"followers": 444}
    result = calculate_codex_score(fake_profile, [])
    assert result == 0

    print("All tests passed")

test_codex_score_empty_repos()

from summarizer import get_star_tier, get_account_age
def test_get_star_tier():
    assert get_star_tier(0) == "emerging developer"
    assert get_star_tier(50000) == "top 1% on Github"
    assert get_star_tier(500) == "recognised developer"

    print("All tests passed")

test_get_star_tier()

def test_get_account_age():
    assert get_account_age("2010-01-01T00:00:00Z") == "veteran of the community"
    assert get_account_age("2024-01-01T00:00:00Z") == "relatively new to Github"

    print("All tests passed")

test_get_account_age()