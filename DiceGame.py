import random as r

dice1 = r.randint(1,6)
dice2 = r.randint(1,6)
total = dice1+dice2

print('What is your name?')
print('>',end='')
Name = input()
print('Hello,{}!'.format(Name))

print('Rolling the dice...')
print('Die1 :{}'.format(dice1))
print('Die2 :{}'.format(dice2))
print('Total value:{}'.format(total))

