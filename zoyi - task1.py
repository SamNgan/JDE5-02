import random

text = './news.txt'
f = open(text, "r")
f2 = f.read()
print(f.read())

def hammer_pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result


if __name__ == "__main__":
    print(hammer_pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    print('a', (f2.count('a')))
    print('e', (f2.count('e')))
    print('i', (f2.count('i')))
    print('o', (f2.count('o')))
    print('u', (f2.count('u')))

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

  
    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob