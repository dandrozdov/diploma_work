from src.main import app
from src.config import TELEGRAM_MESSAGE_LIMIT


def test_endpoint():
    test_client = app.test_client()
    message_to_telegram = 'a' * 3 * TELEGRAM_MESSAGE_LIMIT
    response = test_client.post('/', json={'message': message_to_telegram})
    assert response.status_code == 200
    assert response.json == {'result': 'Message sended to Telegram.'}
