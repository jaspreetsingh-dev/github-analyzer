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
