from jobhunt.digest import _card
from jobhunt.fetch import Job


def _job(salary=None):
    return Job(
        job_id="ashby:test:1",
        ats="ashby",
        company="Test",
        title="Machine Learning Engineer",
        location="Hyderabad",
        url="https://example.com",
        description="",
        salary=salary,
    )


def test_card_displays_published_compensation():
    assert "INR 50,000/month" in _card(_job("INR 50,000/month"))


def test_card_labels_missing_compensation_honestly():
    assert "Not published by employer" in _card(_job())
