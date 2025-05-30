# tests/test_utils.py
from src.utils import get_project_name

def test_get_project_name():
    assert get_project_name() == "News Sentiment Stock Movement"
