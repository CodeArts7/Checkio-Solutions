def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=get_name, reverse=True)[:limit]
    #return sorted(data, key=lambda d: d['price'], reverse=True)[:limit]
    #import operator and return sorted(data, key=operator.itemgetter("price»), reverse=True)[:limit)



def get_name(data):
    return data["price"]


print(bigger_price(2,
    [{"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}]))