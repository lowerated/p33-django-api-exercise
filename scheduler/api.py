import requests

def get_eld_data(access_token, endpoint):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f"{endpoint}/trucks", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
