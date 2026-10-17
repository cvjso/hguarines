FROM nginx:alpine

# Remove a página padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia o HTML compilado com todos os assets para a raiz web do Nginx
COPY siga_upe_completo.html /usr/share/nginx/html/index.html

# Expõe a porta 80 HTTP
EXPOSE 80

# Inicia o Nginx em primeiro plano
CMD ["nginx", "-g", "daemon off;"]
