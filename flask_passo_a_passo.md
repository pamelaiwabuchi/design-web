# Tutorial Flask

## Preparação do ambiente

Não devemos instalar bibliotecas diretamente no sistema global para não "poluir" a máquina. Sendo assim, criamos um ambiente virtual (`venv`) e instalamos tudo o que precisamos lá.

```bash
# 1. Cria o ambiente virtual (igual para todos os sistemas)
python -m venv .venv

# 2. Ativa o ambiente

# Linux:
source venv/bin/activate

# Windows:
.\venv\Scripts\activate

# 3. Com o ambiente venv ativado, vamos iniciar a instalação
# seu terminal deve começar com (venv)
pip install flask
```
Para mais informações e detalhes: 
https://flask.palletsprojects.com/en/stable/installation/

## Estrutura de Aplicação e Rotas

1. Passo 1: Criar arquivo app.py
- No arquivo app.py definimos as rotas do site, essa é a estrutura básica padrão dele:

```python
from flask import Flask, render_template

# Inicializa a aplicação
app = Flask(__name__)

# Define a rota principal (home) - se quiser criar a página "Deputados", a rota será /deputados

@app.route("/")
def home():
    return render_template("index.html")
    # O render_template busca automaticamente arquivos dentro da pasta /templates - pra isso, o flask segue uma estrutura rígida de pastas que veremos no próximo passo
```    

Para vermos se deu certo, rode um destes comandos no terminal com o venv ativado:
``` bash
#forma simples:
python3 app.py

#com debug:
flask --app app --debug run
#Atenção: No comando flask --app app, o segundo app refere-se ao nome do seu arquivo. Se o seu arquivo for index.py, use flask --app index --debug run.

#usamos o debug porque com ele, o servidor reinicia automaticamente toda vez que você salva um arquivo. Sem o debug, você precisaria encerrar o terminal e rodar o comando novamente a cada pequena mudança no HTML ou Python.
```
Para mais detalhes:
https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode

Para encerrar o servidor -> Ctrl + C

## Organização de pastas (Obrigatório)

Por padrão, o flask exige:

`/templates` -> para arquivos html.

`/static` -> para arquivos que o navegador precisa carregar diretamente. Ex: imagens, css, JavaScript, etc.

## Delimitadores de Template

### Base Template - Jinja2

Recomendação de vídeo:
https://www.youtube.com/watch?v=epTuwBcfjJk


O template chamado `base.html` define o esqueleto HTML simples. Por exemplo:

A barra de navegação e o rodapé se repetem em todas as páginas do site. Ao invés de copiar e colar a estrutura em cada página - o que implica em alterar uma mudança em cada página manualmente - podemos simplesmente colocá-las no arquivo base.html. Assim, se precisarmos mudar o nome da página de "Contato" para "Contate-nos", realizamos a mudança apenas no arquivo base. 

Cada arquivo como quemsomos.html e contato.html contém apenas o que é único da sua página, como form apenas no contato.html e texto institucional apenas no quemsomos.html.

Mais informações aqui:
https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance

```html
<!DOCTYPE html>
<html lang="en">
<head>
<!--
Tudo o que está entre o block head e o endblock é o conteúdo padrão que será exibido se uma página filha não definir nada.
-->
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
</html>


```
