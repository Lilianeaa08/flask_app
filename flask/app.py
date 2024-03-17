from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from openai_api import analise_openai

app = Flask(__name__)
client = MongoClient("mongodb://mongodb:27017/")
db = client['meu_banco']  
collection = db['dados_collection']  

@app.route('/')
def index():
    documento = collection.find_one(sort=[('_id', -1)]) 
    recomendacao = documento['recomendacao'] if documento else None
    return render_template('index_mongodb.html', recomendacao=recomendacao)

@app.route('/adicionar_dado', methods=['POST'])
def adicionar_dado():
    conteudo = request.form['conteudo']
    resultado = analise_openai(conteudo)
    novo_dado = {'conteudo': conteudo,'recomendacao':resultado}
    collection.insert_one(novo_dado) 
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)