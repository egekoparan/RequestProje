###https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json
import requests

def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()  # Veri burada döndürülmeli
    else:
        print("Failed to fetch data.")
        return []  # Boş liste döndürmek güvenli olur

crypto_response = get_crypto_data()
user_input = input("Enter a crypto currency: ")

for crypto in crypto_response:
    if crypto["currency"].lower() == user_input.lower():
        print(f"Price of {user_input} is {crypto['price']}")
        break
else:
    print(f"{user_input} not found.")
