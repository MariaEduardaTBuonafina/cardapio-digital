# Importamos as ferramentas que vamos usar
from flask import Flask, jsonify  # Flask cria o servidor; jsonify converte dados para JSON
from flask_cors import CORS        # Permite que o frontend acesse o backend
import os                          # Permite acessar variáveis de ambiente

# Criamos a aplicação Flask
app = Flask(__name__)

# Ativamos o CORS para que o frontend possa fazer requisições ao backend
CORS(app)

# -------------------------------------------------------
# DADOS DO CARDÁPIO
# Em um projeto real, esses dados viriam de um banco de dados.
# Para o nosso projeto, vamos deixar os dados aqui no código mesmo.
# -------------------------------------------------------
cardapio = {
    "restaurante": "Cantina da Squad",
    "categorias": [
        {
            "nome": "🍕 Entradas",
            "itens": [
                {"id": 1, "nome": "Bruschetta", "descricao": "Pão tostado com tomate e manjericão", "preco": 18.90},
                {"id": 2, "nome": "Bolinha de Queijo", "descricao": "Crocante por fora, derretida por dentro", "preco": 22.00},
                {"id": 3, "nome": "Salada Caesar", "descricao": "Alface, croutons, parmesão e molho especial", "preco": 28.50}
            ]
        },
        {
            "nome": "🍝 Pratos Principais",
            "itens": [
                {"id": 4, "nome": "Macarrão ao Sugo", "descricao": "Massa artesanal com molho de tomate fresco", "preco": 42.00},
                {"id": 5, "nome": "Frango Grelhado", "descricao": "Com arroz, feijão e farofa", "preco": 48.90},
                {"id": 6, "nome": "Filé ao Molho Madeira", "descricao": "Filé mignon com batatas rústicas", "preco": 68.00},
                {"id": 7, "nome": "Peixe na Brasa", "descricao": "Tilápia com legumes salteados", "preco": 55.00}
            ]
        },
        {
            "nome": "🍰 Sobremesas",
            "itens": [
                {"id": 8, "nome": "Pudim de Leite", "descricao": "Receita da vovó, calda de caramelo", "preco": 16.00},
                {"id": 9, "nome": "Petit Gâteau", "descricao": "Bolo quente com sorvete de creme", "preco": 28.00},
                {"id": 10, "nome": "Mousse de Maracujá", "descricao": "Leve e refrescante", "preco": 18.00}
            ]
        },
        {
            "nome": "🥤 Bebidas",
            "itens": [
                {"id": 11, "nome": "Suco Natural", "descricao": "Laranja, limão ou maracujá", "preco": 12.00},
                {"id": 12, "nome": "Refrigerante", "descricao": "Lata 350ml", "preco": 8.00},
                {"id": 13, "nome": "Água Mineral", "descricao": "Com ou sem gás 500ml", "preco": 6.00}
            ]
        }
    ]
}

# -------------------------------------------------------
# ROTAS (endpoints) da API
# Uma "rota" é um endereço que o frontend pode acessar.
# O símbolo @ antes da função é chamado de "decorator" — ele
# diz ao Flask: "quando alguém acessar essa URL, execute essa função".
# -------------------------------------------------------

# Rota principal — só para testar se o servidor está funcionando
@app.route('/')
def inicio():
    # jsonify transforma o dicionário Python em formato JSON
    return jsonify({"mensagem": "API do Cardápio funcionando!", "status": "ok"})

# Rota que retorna todo o cardápio
@app.route('/cardapio')
def get_cardapio():
    return jsonify(cardapio)

# Rota que retorna um item específico pelo ID
@app.route('/item/<int:item_id>')
def get_item(item_id):
    # Percorremos todas as categorias e todos os itens
    for categoria in cardapio["categorias"]:
        for item in categoria["itens"]:
            if item["id"] == item_id:
                return jsonify(item)
    # Se não encontrou, retorna erro 404
    return jsonify({"erro": "Item não encontrado"}), 404

# -------------------------------------------------------
# INICIALIZAÇÃO DO SERVIDOR
# Este bloco só executa quando rodamos "python app.py" diretamente.
# A variável PORT vem do arquivo .env (ou usa 5000 como padrão).
# -------------------------------------------------------
if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=porta, debug=True)