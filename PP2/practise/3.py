import re
'''
text = "aaaacbbbbb"
x = re.search('a*b*', text)
print(x)
'''
text = ('abbabbb')
x = re.search('abb|abbb', text)
print(x)