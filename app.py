from flask import Flask, request, redirect, render_template, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para usar flash messages

# Configuração do Banco de Dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Insira sua senha do MySQL, se houver
app.config['MYSQL_DB'] = 'confeitaria'

mysql = MySQL(app)

@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT nome, nota, comentario, data_envio FROM avaliacoes ORDER BY data_envio DESC")
        avaliacoes = cur.fetchall()
        cur.close()
        return render_template('index.html', avaliacoes=avaliacoes)
    except Exception as e:
        flash(f"Erro ao carregar avaliações: {e}", "danger")
        return render_template('index.html', avaliacoes=[])

@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        nota = request.form.get('nota')
        comentario = request.form.get('comentario')

        # Adicione prints para depuração
        print(f"Dados recebidos do formulário: Nome={nome}, Nota={nota}, Comentário={comentario}")

        # Validação dos dados
        if not nome or not nota or not comentario:
            flash("Todos os campos são obrigatórios!", "warning")
            print("Erro: Campos obrigatórios estão faltando.")
            return redirect('/')

        try:
            # Inserir dados no banco
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO avaliacoes (nome, nota, comentario, data_envio) VALUES (%s, %s, %s, NOW())",
                (nome, nota, comentario)
            )
            mysql.connection.commit()
            cur.close()
            flash("Avaliação enviada com sucesso!", "success")
            print("Avaliação inserida com sucesso no banco!")
        except Exception as e:
            flash(f"Erro ao enviar avaliação: {e}", "danger")
            print(f"Erro ao inserir no banco: {e}")

        return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)
