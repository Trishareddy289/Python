#fantasygameinventor

print("K.trisha,USN:1AY24AI051,SEC:M")

game_inventory = {'rope' : 1,'gold coin' : 42}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory,addItems):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        if k in addItems:
            0==addItems.count(k)
            inventory[k]=v+0
    for k2 in addItems:
        if k2 not in inventory.keys():
            inventory[k2]=addItems.count(k2)
    for k3, v2 in inventory.items():
        print(v2,k3)
        total += v2
    print('the total no of items is: ' + str(total))
addToInventory(game_inventory,dragon_loot)
    

   
