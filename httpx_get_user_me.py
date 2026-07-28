import httpx

BASE_URL = "http://localhost:8000"

login_payload = {
    "email": "user11@example.com",
    "password": "123"
}

login_response = httpx.post(f"{BASE_URL}/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login status code:", login_response.status_code)
print("Login response:", login_response_data)

access_token = login_response_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_token}"}
user_me_response = httpx.get(f"{BASE_URL}/api/v1/users/me", headers=headers)
user_me_response_data = user_me_response.json()

print("User me status code:", user_me_response.status_code)
print("User me response:", user_me_response_data)
