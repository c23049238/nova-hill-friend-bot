import requests

your_token = "your_token_here" #go to network tab, send a friend request to someone and find the token you got from the payload
your_cookie = "your_cookie_here" # put your nova_hill_session cookie here
start_user_id = 1 # adjust this to what user id you want to start at
end_user_id = 100 # adjust this to what user id you want to end at, so if you want to friend the entire website just put an amount you know is higher instead of counting users manually

url = "https://nova-hill.com/friends/update"
payload = {
    "_token": your_token,
    "id": "1",
    "action": "send"
}

headers = {
    "Cookie": f"nova_hill_session={your_cookie}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def send_friend_request(user_id):
    payload["id"] = str(user_id)
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        print(f"Friend request sent to user id {user_id}")
    else:
        print(f"Failed to send friend request to user id {user_id} - Status Code: {response.status_code}")
    return response.status_code, response.text

for user_id in range(start_user_id, end_user_id + 1):
    send_friend_request(user_id)
