# Sistema de Gestão de Rotas e Fretes

## Descrição

Sistema web simples para gestão de rotas e fretes com interface interativa mostrando as áreas de representação da empresa em todo o Brasil e Colômbia.

## Funcionalidades

- 🗺️ **Mapa Interativo do Brasil**: Visualização de todos os estados brasileiros organizados por região
- 🇨🇴 **Representação Internacional**: Cobertura na Colômbia
- 📞 **Formulário de Contato**: Sistema completo para receber solicitações de clientes
- 🚚 **Gestão de Fretes**: Interface para consultas sobre rotas e fretes

## Como Executar

### Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o sistema:
```bash
cd sistema_rotas_fretes
python app.py
```

3. Acesse no navegador:
```
http://localhost:5000
```

## Estrutura do Projeto

```
sistema_rotas_fretes/
├── app.py                 # Aplicação Flask principal
└── templates/
    └── index.html        # Interface web com mapa e formulário
```

## Recursos

### Representação Geográfica

O sistema possui cobertura em:
- **Brasil**: Todos os 26 estados + Distrito Federal
  - Norte: AC, AM, AP, PA, RO, RR, TO
  - Nordeste: AL, BA, CE, MA, PB, PE, PI, RN, SE
  - Centro-Oeste: DF, GO, MT, MS
  - Sudeste: ES, MG, RJ, SP
  - Sul: PR, RS, SC
- **Colômbia**: Representação internacional

### Formulário de Contato

O formulário permite:
- Seleção do estado/país
- Tipos de assunto: orçamento, rotas, frete, representação comercial
- Validação de dados
- Feedback visual para o usuário

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Gradientes modernos e design responsivo

## API Endpoints

- `GET /`: Página principal
- `GET /api/representacoes`: Retorna dados de representações em JSON
- `POST /api/contato`: Processa formulário de contato
- `GET /api/contatos`: Lista contatos recebidos

## Próximas Melhorias

- Integração com banco de dados
- Sistema de autenticação
- Dashboard administrativo
- Cálculo automático de rotas e fretes
- Integração com APIs de mapas (Google Maps, Mapbox)
- Sistema de rastreamento de entregas

## Autor

Sistema desenvolvido como parte dos estudos em Python.
