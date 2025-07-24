from hexlet_pytest.example import reverse
from pathlib import Path

def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""

def get_path(file_name):
    return Path(__file__).parent / "test_data" / file_name

def test_progress():
    text_in = get_path("test_reverse_before.txt").read_text()
    text_out = get_path("test_reverse_after.txt").read_text()

    actual = reverse(text_in)

    assert actual.strip() == text_out.strip()
 

