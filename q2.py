#category wise price calculator

def get_category_total_price(category):

grocery_total_price=0
for item in grocery_data:
    if item["category"]==category:
        

        total_price=item["price"]*item["quanity"]
        grocery_total_price+=total_price
return grocery_total_price

