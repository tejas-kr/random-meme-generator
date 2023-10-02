import pytest
from unittest.mock import Mock, patch
from unittest import TestCase
from meme_url_grabber import Meme
from app import app

mock_get_meme = Mock(
    return_value=iter([("Test Meme Text", "https://dummy.com/images/meme/testmeme",)])
)

mock_get_meme_count_2 = Mock(
    return_value=iter([
        ("Test Meme Text", "https://dummy.com/images/meme/testmeme",),
        ("Test Meme Text2", "https://dummy.com/images/meme/testmeme2",)
    ])
)


@pytest.fixture()
def client():
    return app.test_client()



URL: str = "/memes"
VALID_RESP_COUNT_1 = {
    "1": {
        "link": "https://dummy.com/images/meme/testmeme",
        "text": "Test Meme Text"
    }
}

VALID_RESP_COUNT_2 = {
    "1": {
        "link": "https://dummy.com/images/meme/testmeme",
        "text": "Test Meme Text"
    },
    "2": {
        "link": "https://dummy.com/images/meme/testmeme2",
        "text": "Test Meme Text2"
    }
}

@patch.object(Meme, 'get_memes', mock_get_meme)
def test_meme_gen_valid(client): 
    resp = client.get(URL)

    assert resp.json == VALID_RESP_COUNT_1
    assert resp.status == "200 OK"

@patch.object(Meme, 'get_memes', mock_get_meme_count_2)
def test_meme_gen_valid_count_2(client): 
    resp = client.get(URL)

    assert resp.json == VALID_RESP_COUNT_2
    assert resp.status == "200 OK"
