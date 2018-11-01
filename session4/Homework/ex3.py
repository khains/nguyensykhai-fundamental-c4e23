prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
total = 0
for k in prices.keys():
    for v in stock.keys():
        if k == v:
            print(k, prices[k], stock[v])
            s = prices[k] * stock[v]
            total += s
print("total = ", total)
               