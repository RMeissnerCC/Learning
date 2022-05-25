vowels = ['a', 'e', 'i', 'o', 'u']
characters = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(lambda x: True if x in vowels else False, characters)

print('The filtered letters are:')

[print(s) for s in filtered]
