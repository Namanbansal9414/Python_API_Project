import requests

def get_random_product_api():
    url ="https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data :
        user = data["data"]
        product_name = user["title"]
        product_description = user["description"]
        product_price = user["price"]
        discount = user["discountPercentage"]
        product_rating = user["rating"]
        product_category = user["category"]
        return product_name, product_description, product_price, discount, product_rating, product_category
    else:
        raise Exception("Failed to retrieve product data")

def main():
    try:
        product_name, product_description, product_price, discount, product_rating, product_category = get_random_product_api()
        print(f"Product Name: {product_name}")
        print(f"Product Description: {product_description}")
        print(f"Product Price: {product_price*100}")
        print(f"Discount Percentage : {discount}%")
        print(f"Product Rating: {product_rating}/5")
        print(f"Product Category: {product_category}")
    except Exception as e:
        print(f"An error occurred : {str(e)}")


if __name__ =="__main__":
    main()