import requests
from bs4 import BeautifulSoup
# alexa
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, "/ludonews")





pagina = "https://www.ludopedia.com.br/canal/ludonews&id_categoria_canal=572"
req = requests.get(pagina)

soup = BeautifulSoup(req.text, 'html.parser')



def getLudoNews():
    lista = []
    dados = soup.find_all(class_="row")
    for news in dados:
        noticias = news.get_text().replace("LudoNews","")
        lista.append(noticias)
        #print(lista)
        return str(lista).replace('\\n', ' ')

@app.route('/')
def homepage():
    return "site ok!"


@ask.launch 
def start_skill():
    msg = "Bem vindo ao Ludonews! O que deseja?"
    return question(msg)

@ask.intent("YesIntent")
def getnews():
    msg = getLudoNews()
    head_msg = "As noticias sao: {}".format(msg)
    return statement(head_msg)




if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)


