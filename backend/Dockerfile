
FROM python:3.11-slim

# Definimos a pasta de trabalho dentro do container
WORKDIR /app


COPY requirements.txt .

# Instalamos as dependências Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]