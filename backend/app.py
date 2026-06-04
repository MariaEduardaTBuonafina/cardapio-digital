# Importando as ferramentas 
from flask import Flask, jsonify  
from flask_cors import CORS        
import os                          

# Criando a aplicação Flask
app = Flask(__name__)

CORS(app)

# DADOS DO CARDÁPIO

cardapio = {
    "restaurante": "Cantina",
    "categorias": [
        {
            "nome": "🍕 Entradas",
            "itens": [
                {"id": 1, "nome": "Bruschetta", "descricao": "Pão tostado com tomate e manjericão", "preco": 10.00},
                {"id": 2, "nome": "Bolinha de Queijo (Porção)", "descricao": "Crocante por fora, derretida por dentro", "preco": 22.00},
                {"id": 3, "nome": "Salada Caesar", "descricao": "Alface, croutons, parmesão e molho especial", "preco": 15.00}
            ]
        },
        {
            "nome": "🍝 Pratos Principais",
            "itens": [
                {"id": 4, "nome": "Macarrão ao Sugo", "descricao": "Massa artesanal com molho de tomate fresco", "preco": 25.00},
                {"id": 5, "nome": "Frango Grelhado", "descricao": "Com arroz, feijão e farofa", "preco": 30.00},
                {"id": 6, "nome": "Filé ao Molho Madeira", "descricao": "Filé mignon com batatas rústicas", "preco": 50.00},
                {"id": 7, "nome": "Peixe na Brasa", "descricao": "Tilápia com legumes salteados", "preco": 50.00}
            ]
        },
        {
            "nome": "🍰 Sobremesas",
            "itens": [
                {"id": 8, "nome": "Pudim de Leite", "descricao": "Receita da vovó, calda de caramelo", "preco": 10.00},
                {"id": 9, "nome": "Petit Gâteau", "descricao": "Bolo quente com sorvete de creme", "preco": 20.00},
                {"id": 10, "nome": "Mousse de Maracujá", "descricao": "Leve e refrescante", "preco": 8.00}
            ]
        },
        {
            "nome": "🥤 Bebidas",
            "itens": [
                {"id": 11, "nome": "Suco Natural", "descricao": "Laranja, limão ou maracujá", "preco": 5.00},
                {"id": 12, "nome": "Refrigerante", "descricao": "Lata 350ml", "preco": 3.50},
                {"id": 13, "nome": "Água Mineral", "descricao": "Com ou sem gás 500ml", "preco": 2.00}
            ]
        }
    ]
}

# ROTAS 


# Rota principal 
@app.route('/')
def inicio():
    return jsonify({"mensagem": "API do Cardápio funcionando!", "status": "ok"})

# Rota que retorna todo o cardápio
@app.route('/cardapio')
def get_cardapio():
    return jsonify(cardapio)

# Rota que retorna um item específico pelo ID
@app.route('/item/<int:item_id>')
def get_item(item_id):
    for categoria in cardapio["categorias"]:
        for item in categoria["itens"]:
            if item["id"] == item_id:
                return jsonify(item)
    return jsonify({"erro": "Item não encontrado"}), 404

# INICIALIZAÇÃO DO SERVIDOR

if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=porta, debug=True)