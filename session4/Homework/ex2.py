inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory["pocket"] = ['seashell', 'strange berry', 'lint']
v = inventory["backpack"]
v.remove("dagger")
inventory["gold"] = 500, 50
for k, v in inventory.items():
    print(k,":", v)
