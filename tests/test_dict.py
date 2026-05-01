"""Tests for dict.py"""
import subprocess
import sys


def test_lookup_exists():
    result = subprocess.run([sys.executable, "dict.py", "ном"],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "book" in result.stdout


def test_lookup_reverse():
    result = subprocess.run([sys.executable, "dict.py", "--reverse", "book"],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "ном" in result.stdout


if __name__ == "__main__":
    test_lookup_exists()
    test_lookup_reverse()
    print("Бүх тест амжилттай ✓")
