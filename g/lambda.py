# dictionaries inside list
people=[
    {"name":"sukku","home":"mokama"},
    {"name":"janu","home":"nellore"},
    {"name":"aamir","home":"katihaar"}
]
print(people.sort())
# want to print this list in sorted order
# but we cant compare 2 dictonaries we will get <type error

'''
def sort_func(person):
    return person["name"] 

people.sort(key=sort_func)

'''

people.sort(key=lambda person: person["name"])
print(people)