from flask import Flask, render_template, request, redirect, url_for #request lê os dados, redirect e url_for redirecionam após salvar, lê as variaveis de ambiente da railway
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST"),
        port=int(os.environ.get("MYSQLPORT", 3306)), 
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE")
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        sugestao = request.form.get("sugestao")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO unitev (nome, email, sugestao) VALUES (%s, %s, %s)",
            (nome, email, sugestao)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("contato"))
    return render_template("contato.html")
    
@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))