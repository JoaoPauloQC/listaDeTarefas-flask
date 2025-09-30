from flask import (render_template,request,redirect,url_for,flash,abort,jsonify,session)

from app import app

TAREFAS_DB = {
    1: {'texto': "Aprender os conceitos do Flask", 'concluida': True},
    2: {'texto': "Ver os exemplos de codigo", 'concluida': False},
    3: {'texto': "Construir minha própria aplicação", 'concluida': False},
    
}
next_id = 4

@app.route("/")
def index():
    return render_template("index.html",tarefas=TAREFAS_DB)

@app.route('/tarefa/<int:id>')
def tarefa_detail(id):
    tarefa = TAREFAS_DB.get(id)
    if not tarefa:
        abort(401)
    return render_template('detalhe.html',tarefa = tarefa, tarefa_id = id)

@app.route("/adicionar",methods=['POST'])
def adicionar():
    global next_id
    text_tarefa = request.form.get('texto_da_tarefa')

    if not text_tarefa or len(text_tarefa) < 3:
        flash("A tarefa precisa ter pelo menos 3 caracteres",'erro')
    else:
        TAREFAS_DB[next_id] = {'texto': text_tarefa, 'concluida': False}
        next_id +=1

        flash("Tarefa adicionada com o sucesso!", "sucesso")

        session['contador'] = session.get('contador',0) +1
        flash(f"Voce ja adicionou {session['contador']} tarefas!",'info')
    
    return redirect(url_for("index"))


@app.route("/tarefa/concluir/<int:id>",methods=['POST'])
def concluir_tarefa(id):
    print(id)
    tarefa = TAREFAS_DB.get(id)
    if tarefa:
        tarefa['concluida'] = not tarefa['concluida']
        return jsonify({"Status": "sucesso", "concluida": tarefa['concluida']})
    return jsonify({"Status": "erro"}),404

@app.route("/admin")
def admin_panel():
    if session.get("username") != "admin":
        abort(403)
    return "<h1> Painel de Administrador </h1>"

@app.errorhandler(404)
def not_found_error():
    return render_template("erros/404.html"),404

@app.errorhandler(403)
def forbidden_error():
    return render_template("erros/403.html"),403

@app.errorhandler(401)
def unathorized_error():
    return render_template("erros/401.html"),401


