import requests

# BASE_URL = "http://192.168.20.10"
BASE_URL = input('inserire url:' ) #"http://192.168.20.10/phpMyAdmin/themes/original/img/logo_right.png"

def stampa_risposta(response): #Definisco la risposta ai verbi
    print(f"\n=== {response.request.method} ===")
    print("Status code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text[:200], "...")  # Mostra solo i primi 200 caratteri

def test_get():
    response = requests.get(BASE_URL)
    stampa_risposta(response)

def test_post():
    data = {"username": "test", "password": "1234"}
    response = requests.post(BASE_URL, data=data)
    stampa_risposta(response)

def test_put():
    data = {"update": "true"}
    response = requests.put(BASE_URL, data=data)
    stampa_risposta(response)

def test_delete():
    response = requests.delete(BASE_URL)
    stampa_risposta(response)

def test_head():
    response = requests.head(BASE_URL)
    stampa_risposta(response)

def test_options():
    response = requests.options(BASE_URL)
    stampa_risposta(response)


def main():
    test_get()
    test_post()
    test_put()
    test_delete()
    test_head()
    test_options()

if __name__ == "__main__":
    main()
