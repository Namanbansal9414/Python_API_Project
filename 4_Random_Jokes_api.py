import requests

def get_random_jokes():
    data = requests.get("https://api.freeapi.app/api/v1/public/randomjokes/joke/random").json()

    if data["success"] and "data" in data:
        jokes = data["data"]["content"]
        message = data["message"]
        return jokes, message
    else:
        raise Exception("Failed to retrieve jokes")
    
def main():
    try:
        jokes, message = get_random_jokes()
        print("\n")
        print(f"Joke: {jokes}")
        print("\n")
        print(f"Message: {message}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__=="__main__":
    main()