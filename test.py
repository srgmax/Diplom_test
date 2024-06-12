# Сергей Лобанов, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_response_code():
    track = sender_stand_request.post_new_order(data.order_body).json().get("track")
    order_responce = sender_stand_request.details_order(track).status_code
    assert order_responce == 200
