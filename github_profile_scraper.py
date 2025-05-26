import requests

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract some basic profile data
        profile = {
            "login": data.get("login"),
            "name": data.get("name"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "bio": data.get("bio"),
            "location": data.get("location"),
            "blog": data.get("blog"),
            "created_at": data.get("created_at"),
        }
        return profile
    else:
        print("Failed to fetch profile data")
        return None

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    profile = get_github_profile(username)
    if profile:
        for key, value in profile.items():
            print(f"{key}: {value}")
