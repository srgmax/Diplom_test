# Сергей Лобанов, 17-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_response_code():
    order_responce = sender_stand_request.details_order().status_code
    assert order_responce == 200