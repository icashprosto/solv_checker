import requests
import time
import random
#import os

# Конфигурация
url = "https://sf.sft-api.com/graphql"
headers = {
    "Content-Type": "application/json",
    "Authorization": "dW5kZWZpbmVkfHx1bmRlZmluZWR8fHVuZGVmaW5lZHx8",  # Замените на реальный токен
    "Origin": "https://solv.foundation",
    "Referer": "https://solv.foundation/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}



WALLETS_FILE = "wallets_solv.txt"
RESULT_FILE = "result_solv.txt"

# Функция для выполнения запроса
def check_eligibility(address):
    payload = {
        "operationName": "EligibilityCheck",
        "variables": {
            "address": address
        },
        "query": """query EligibilityCheck($address: String!, $rewardType: String) {
            eligibilityCheck(address: $address, rewardType: $rewardType) {
                stagesInfo {
                    pointSysReward
                }
            }
        }"""
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Проверка статуса ответа
        data = response.json()

        # Извлечение значения 'pointSysReward'
        stages_info = data.get("data", {}).get("eligibilityCheck", {}).get("stagesInfo", [])
        if stages_info:
            point_sys_reward = stages_info[0].get("pointSysReward", "N/A")  # Берем первый элемент
            return point_sys_reward
        else:
            return "No stages info"
    except Exception as e:
        return f"Error: {e}"

# Основной процесс
def main():
    # Чтение списка кошельков из файла
    with open(WALLETS_FILE, "r") as wallets_file:  # Используем WALLETS_FILE
        wallets = [line.strip() for line in wallets_file if line.strip()]

    # Открытие файла для записи результатов
    with open(RESULT_FILE, "w") as result_file:  # Используем RESULT_FILE
        for wallet in wallets:
            print(f"Проверка кошелька: {wallet}")

            # Выполняем запрос
            reward = check_eligibility(wallet)

            # Запись результата в файл
            result_line = f"{wallet} : {reward}\n"
            result_file.write(result_line)
            print(f"Результат: {result_line.strip()}")

            # Пауза 3–5 секунд
            time.sleep(random.uniform(3, 5))

if __name__ == "__main__":
    main()
