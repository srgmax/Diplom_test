import config
import requests


# Создание нового заказа
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                         json=body)


def details_order(trackOrder):
    return requests.get(config.URL_SERVICE + config.GET_ORDER + str(trackOrder))
