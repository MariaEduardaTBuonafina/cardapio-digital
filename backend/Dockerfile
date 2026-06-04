# Usamos uma imagem Python leve como base
# "slim" significa que é uma versão reduzida, sem pacotes desnecessários
FROM python:3.11-slim

# Definimos a pasta de trabalho dentro do container
# Todos os próximos comandos vão rodar dentro de /app
WORKDIR /app

# COPIAMOS o requirements.txt ANTES do resto do código
# Isso é uma otimização: o Docker "cacheia" as camadas.
# Se só mudarmos o app.py, ele não vai reinstalar as dependências.
COPY requirements.txt .

# Instalamos as dependências Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Agora copiamos o resto do código para dentro do container
COPY . .

# Informamos que o container vai usar a porta 5000
EXPOSE 5000

# Comando que será executado quando o container iniciar
CMD ["python", "app.py"]