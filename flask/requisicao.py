from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from openai_api import analise_openai

app = Flask(__name__)
client = MongoClient("mongodb://mongodb:27017/") ##client = MongoClient('mongodb://meu_mongo:27017/')  # Conectando ao servidor MongoDB dentro do Docker
db = client['recomendacao'] 
collection = db['dados_openai']  

@app.route('/')
def index():
    dados = collection.find()
    return render_template('index_mongodb.html', dados=dados)

@app.route('/adicionar_dado', methods=['POST'])
def adicionar_dado():
    conteudo = request.form['conteudo']
    client = MongoClient('mongodb://mongodb:27017/')  
    db = client['recomendacao']  
    collection = db['dados_openai']  
    novo_dado = {'conteudo': conteudo}
    collection.insert_many(novo_dado)
    client.close()  
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)