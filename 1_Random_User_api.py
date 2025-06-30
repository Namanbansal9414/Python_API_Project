import requests

def fectch_random_user_api():
    
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    api = response.json()

    # api = requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random").json()

    if api ["success"] and "data" in api:
        user_data =api["data"]
        name = user_data["name"]["first"]
        surname = user_data["name"]["last"]
        email = user_data["email"]
        username = user_data["login"]["username"]
        password = user_data["login"]["password"]
        country = user_data["location"]["country"]
        return name , surname, email, username, password, country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
       name, surname, email, username, password, country = fectch_random_user_api()
       print(f"Name : {name +" "+surname}")
       print(f"Email : {email}")
       print(f"Username : {username}")
       print(f"Password : {password}")
       print(f"Country : {country}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()

