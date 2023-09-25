def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices
product_list = ['apple', 'banana', 'apple', 'orange', 'apple', 'grape']
target_product = 'apple'

result = linear_search_product(product_list, target_product)

if result:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found.")
