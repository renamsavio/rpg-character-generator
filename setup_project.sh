#!/bin/bash

# Criar diretórios
mkdir -p app/{api/routes,core,models,services}

# Criar arquivos Python vazios
touch app/__init__.py
touch app/api/__init__.py
touch app/api/routes/__init__.py
touch app/core/__init__.py
touch app/models/__init__.py
touch app/services/__init__.py
touch main.py
touch requirements.txt

# Criar ambiente virtual
python -m venv venv

echo "Estrutura do projeto criada com sucesso!"