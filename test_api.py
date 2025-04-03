import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"


def test_api():
    try:
        # Create a user
        user_data = {
            "username": "testuser11",
            "email": "test11@example.com",
            "password": "testpass123",
            "password2": "testpass123",
            "bio": "Test user 11",
        }

        print("Creating user...")
        response = requests.post(f"{BASE_URL}/users/", json=user_data)
        response.raise_for_status()
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

        token = response.json()["token"]
        headers = {
            "Authorization": f"Token {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        # Create a post
        post_data = {"title": "Test Post", "content": "This is a test post content"}

        print("\nCreating post...")
        response = requests.post(f"{BASE_URL}/posts/", headers=headers, json=post_data)
        response.raise_for_status()
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

        # Get the post ID
        post_id = response.json()["id"]

        # Like the post
        print("\nLiking the post...")
        response = requests.post(f"{BASE_URL}/posts/{post_id}/like/", headers=headers)
        response.raise_for_status()
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

        # Get all posts to verify the like count
        print("\nGetting all posts...")
        response = requests.get(f"{BASE_URL}/posts/")
        response.raise_for_status()
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

    except requests.exceptions.RequestException as e:
        print(f"\nError occurred: {str(e)}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            try:
                print(f"Response content: {e.response.json()}")
            except:
                print(f"Response content: {e.response.text}")


if __name__ == "__main__":
    test_api()
