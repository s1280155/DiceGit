import random as r

dice1 = r.randint(1,6)
dice2 = r.randint(1,6)
total = dice1+dice2

print('Rolling the dice...')
print('Die1 :{}'.format(dice1))
print('Die2 :{}'.format(dice2))
print('Total value:{}'.format(total))

