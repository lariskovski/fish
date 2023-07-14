from random import choice

phrase = ['women', 'want', 'me', 'fish', 'fear', 'me']

def scramble(phrase):
    # output = ([choice(phrase) for i in range(len(phrase))])
    output = []
    for _ in range(len(phrase)):
        word = choice(phrase)
        output.append(word)
        phrase.remove(word)
    return output

print(*scramble(phrase))
