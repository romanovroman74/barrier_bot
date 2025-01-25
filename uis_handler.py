import requests
import config

def start_simple_call(contact):
    url = "https://callapi.comagic.ru/v4.0"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "start.simple_call",
        "id": "req1",
        "params": {
            "access_token": config.uis_api_key,
            "first_call": "contact",
            "virtual_phone_number": "73517001117",
            "contact": f"{contact}",
            "operator": "1"
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()

        if response.status_code == 200 and 'result' in response_data:
            print("Звонок успешно инициирован. ID сессии:", response_data["result"]["data"]["call_session_id"])
        else:
            print("Ошибка при инициации звонка:", response_data.get("error", "Неизвестная ошибка"))
    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", str(e))
