from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Dados de representação da empresa
representacoes = {
    "brasil": {
        "estados": [
            {"nome": "Acre", "sigla": "AC", "regiao": "Norte"},
            {"nome": "Alagoas", "sigla": "AL", "regiao": "Nordeste"},
            {"nome": "Amapá", "sigla": "AP", "regiao": "Norte"},
            {"nome": "Amazonas", "sigla": "AM", "regiao": "Norte"},
            {"nome": "Bahia", "sigla": "BA", "regiao": "Nordeste"},
            {"nome": "Ceará", "sigla": "CE", "regiao": "Nordeste"},
            {"nome": "Distrito Federal", "sigla": "DF", "regiao": "Centro-Oeste"},
            {"nome": "Espírito Santo", "sigla": "ES", "regiao": "Sudeste"},
            {"nome": "Goiás", "sigla": "GO", "regiao": "Centro-Oeste"},
            {"nome": "Maranhão", "sigla": "MA", "regiao": "Nordeste"},
            {"nome": "Mato Grosso", "sigla": "MT", "regiao": "Centro-Oeste"},
            {"nome": "Mato Grosso do Sul", "sigla": "MS", "regiao": "Centro-Oeste"},
            {"nome": "Minas Gerais", "sigla": "MG", "regiao": "Sudeste"},
            {"nome": "Pará", "sigla": "PA", "regiao": "Norte"},
            {"nome": "Paraíba", "sigla": "PB", "regiao": "Nordeste"},
            {"nome": "Paraná", "sigla": "PR", "regiao": "Sul"},
            {"nome": "Pernambuco", "sigla": "PE", "regiao": "Nordeste"},
            {"nome": "Piauí", "sigla": "PI", "regiao": "Nordeste"},
            {"nome": "Rio de Janeiro", "sigla": "RJ", "regiao": "Sudeste"},
            {"nome": "Rio Grande do Norte", "sigla": "RN", "regiao": "Nordeste"},
            {"nome": "Rio Grande do Sul", "sigla": "RS", "regiao": "Sul"},
            {"nome": "Rondônia", "sigla": "RO", "regiao": "Norte"},
            {"nome": "Roraima", "sigla": "RR", "regiao": "Norte"},
            {"nome": "Santa Catarina", "sigla": "SC", "regiao": "Sul"},
            {"nome": "São Paulo", "sigla": "SP", "regiao": "Sudeste"},
            {"nome": "Sergipe", "sigla": "SE", "regiao": "Nordeste"},
            {"nome": "Tocantins", "sigla": "TO", "regiao": "Norte"}
        ]
    },
    "colombia": {
        "ativo": True,
        "nome": "Colômbia"
    }
}

# Armazena contatos (em produção, isso seria um banco de dados)
contatos = []

@app.route('/')
def index():
    """Página principal do sistema"""
    return render_template('index.html', representacoes=representacoes)

@app.route('/api/representacoes')
def get_representacoes():
    """API para obter dados de representações"""
    return jsonify(representacoes)

@app.route('/api/contato', methods=['POST'])
def enviar_contato():
    """Processa o formulário de contato"""
    try:
        dados = request.get_json()
        
        # Validação básica
        if not dados.get('nome') or not dados.get('email') or not dados.get('mensagem'):
            return jsonify({
                'sucesso': False, 
                'mensagem': 'Por favor, preencha todos os campos obrigatórios'
            }), 400
        
        # Adiciona timestamp
        dados['data'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Armazena o contato
        contatos.append(dados)
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'Contato enviado com sucesso! Entraremos em contato em breve.'
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao processar contato: {str(e)}'
        }), 500

@app.route('/api/contatos')
def listar_contatos():
    """Lista todos os contatos recebidos"""
    return jsonify(contatos)

if __name__ == '__main__':
    print("Sistema de Gestão de Rotas e Fretes")
    print("Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
