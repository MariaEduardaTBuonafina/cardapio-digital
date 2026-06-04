# Usamos o Nginx: um servidor web leve e muito rápido
# "alpine" é uma versão ultra-leve do Linux (só ~5MB!)
FROM nginx:alpine

# Copiamos nosso HTML para dentro do servidor Nginx
# O Nginx serve arquivos que estão em /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html

# O Nginx usa a porta 80 por padrão
EXPOSE 80

# Não precisamos definir CMD aqui porque a imagem do Nginx
# já tem o comando padrão de inicialização configurado