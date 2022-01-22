import random, string, pprint
from flask import Flask, render_template, request

letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm '

app = Flask(__name__)
personWords = str(open('personality.txt').read()).split('\n')

def regenWordList():
    global personWordsByLetter
    personWordsByLetter = {}
    for i in string.ascii_lowercase:
        personWordsByLetter[i] = [x for x in personWords if x.startswith(i)]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def acrostic():
    regenWordList()
    poem = []
    name = request.form['name']
    if True:

        l = list(name.lower())
        for i in l:
            if i not in letters:
                continue
            if i == ' ':
                poem.append('\n')
                continue
            if len(personWordsByLetter[i]) == 0:
                return render_template('index.html', log='Sorry, but we couldn\'t generate an acrostic for the name "' + name + '" . Please try again.')
            l = random.choice(personWordsByLetter[i])
            if l in poem:
                personWordsByLetter[i].remove(l)
                if len(personWordsByLetter[i]) <= 0:
                    pprint.pprint(personWordsByLetter, i)
                    return render_template('index.html', log='Sorry, but we couldn\'t generate an acrostic for the name "' + name + '" . Please try again.')
                l = random.choice(personWordsByLetter[i])
            poem.append(l)
        newPoem = ''
        print(poem)
        for line in poem:
            if line == '\n':
                newPoem += '\n'
                continue
            newPoem += f'{line[0].upper()}{line[1:]}\n\n'
            newPoem = newPoem[:-1]  
        print(newPoem) 
        return render_template('index.html', poem=newPoem)
