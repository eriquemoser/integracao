#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

alunos = [
{'id':1, 'nome':'alice', 'curso':'Engenharia de Controle e Automação', 'idade':20},
{'id':2, 'nome':'bob', 'curso':'Engenharia de Materiais', 'idade':18}
]

@app.route('/alunos/getalunos', methods=['GET'])
def get_alunos():
	return jsonify({'alunos':alunos})

#continua na próxima página...

# ...continuação

@app.route('/alunos/getaluno/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
	a = None
	for aluno in alunos:
		if aluno['id'] == aluno_id:
			a = aluno
	if a == None:
		abort(404)
	return jsonify(a)

@app.route('/alunos', methods=['POST'])
def create_aluno():
	if not request.json or not 'nome' in request.json or not 'curso' in request.json:
		abort(400)
	aluno = { 'id': alunos[-1]['id']+1,
		'nome': request.json['nome'],
		'curso': request.json['curso'],
		'idade': request.json['idade']
		}
	alunos.append(aluno)
	return jsonify({'aluno':aluno}),201


if __name__ == '__main__':
	app.run(host='localhost', port=8081, debug=True)
