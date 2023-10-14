import re
imput_string = "How I want a drink, alcoholic of course, after the heavy chapters involving \
quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."
string = re.sub(r'[^\w\s]', '', imput_string)
words = string.split(" ")
result = list(map(len, words))
for word in result:
    print(word, end = "")
