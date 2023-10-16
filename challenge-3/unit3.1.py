def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["pencil", "pen", "eraser", "pencil", "box", "pencil"]
target = "pencil"
target2 = 'marker'
result = linearSearchProduct(products, target)
print(result)