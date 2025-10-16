#!/bin/bash
# Script para iniciar o Sistema de Gestão de Rotas e Fretes

echo "=========================================="
echo "Sistema de Gestão de Rotas e Fretes"
echo "=========================================="
echo ""

# Verifica se o Flask está instalado
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Flask não está instalado. Instalando dependências..."
    pip install -r requirements.txt
    echo ""
fi

echo "Iniciando o sistema..."
echo ""
cd sistema_rotas_fretes
python3 app.py
