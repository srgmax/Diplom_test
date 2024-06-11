import config
import requests
import data

# Создание нового заказа
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                         json=body)

def details_order():
    track = post_new_order(data.order_body).json().get("track")
    return requests.get(config.URL_SERVICE + config.GET_ORDER + str(track))