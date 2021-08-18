import requests

def login(email, password):
    params = {"email": email, "password": password}
    result = requests.post("https://gamermine.com/api/v1/sessions", json = params)
    result.raise_for_status()
    return result.json()["access_token"]

def getMyData(token):
    headers={"authorization": "Bearer "+token}
    result = requests.get("https://gamermine.com/api/v1/users/@me", headers=headers)
    result.raise_for_status()
    return result.json()

def claimDailyBonus(token):
    headers={"authorization": "Bearer "+token}
    result = requests.post("https://gamermine.com/api/v1/daily_bonus/claim", headers=headers)
    result.raise_for_status()

def getInfoAboutDailyBonus(token):
    headers={"authorization": "Bearer "+token}
    result = requests.get("https://gamermine.com/api/v1/daily_bonus", headers=headers)
    result.raise_for_status()
    return result.json()