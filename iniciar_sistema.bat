@echo off
REM Script para iniciar o Sistema de Gestão de Rotas e Fretes no Windows

echo ==========================================
echo Sistema de Gestão de Rotas e Fretes
echo ==========================================
echo.

REM Verifica se o Flask está instalado
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo Flask não está instalado. Instalando dependências...
    pip install -r requirements.txt
    echo.
)

echo Iniciando o sistema...
echo.
cd sistema_rotas_fretes
python app.py
