
from flask import request, jsonify

from helpers.application import app

from controllers.crud import *

from models.Categoria import Categoria
from models.Produto import Produto
from models.Setor import Setor
from models.Usuario import Usuario

@app.route('/')
def homeResource():
    aplicacao = {'versão': '1.0'}
    return jsonify(aplicacao), 200

# CATEGORIA
@app.get('/categoria')
def categorias_get():
    categorias = get_all(Categoria)
    try:
        categoriasJSON = jsonify([vars(categoria) for categoria in categorias])
        return categoriasJSON, 200
    except:
        return categorias
    
@app.get('/categoria/<int:id>')
def categoria_get(id):
    categoria = get_by_ID(Categoria, id)
    try:
        if(categoria):
            return jsonify(vars(categoria))
        else:
            return (jsonify({'mensagem': 'Categoria não encontrada'}), 404)
    except:
        return categoria
    
@app.post('/categoria')
def categoria_post():
    try:
        newCategoria = request.json
        newCategoria = create_item(Categoria, newCategoria)
        return jsonify({'Mensagem': 'Nova categoria criada','Nova Categoria': vars(newCategoria)}), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
@app.put('/categoria/<int:id>')
def categoria_put(id):
    updtCategoria = request.json
    categoria = update_item(Categoria, id, updtCategoria)
    try:
        if(categoria):
            return jsonify({'Mensagem': 'Categoria atualizada','Categoria': vars(categoria)}), 201
    except:
        return categoria
    
@app.delete('/categoria/<int:id>')
def categoria_delete(id):
    delCategoria = delete_item(Categoria, id)
    try:
        return jsonify({'Mensagem': 'Removido com sucesso', 'Categoria removida': vars(delCategoria)})
    except:
        return delCategoria


#  PRODUTOS
@app.get('/produto')
def produtos_get():
    produtos = get_all(Produto)
    try:
        produtosJSON = jsonify([vars(produto) for produto in produtos])
        return produtosJSON, 200
    except:
        return produtos
    
@app.get('/produto/<int:id>')
def produto_get(id):
    produto = get_by_ID(Produto, id)
    try:
        if(produto):
            return jsonify(vars(produto))
        else:
            return (jsonify({'mensagem': 'Produto não encontrado'}), 404)
    except:
        return produto
    
@app.post('/produto')
def produto_post():
    try:
        newProduto = request.json
        newProduto = create_item(Produto, newProduto)
        return jsonify({'Mensagem': 'Novo produto criado','Novo Produto': vars(newProduto)}), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
@app.put('/produto/<int:id>')
def produto_put(id):
    updtProduto = request.json
    produto = update_item(Produto, id, updtProduto)
    try:
        if(produto):
            return jsonify({'Mensagem': 'Produto atualizado','Produto': vars(produto)}), 201
    except:
        return produto
    
@app.delete('/produto/<int:id>')
def produto_delete(id):
    delProduto = delete_item(Produto, id)
    try:
        return jsonify({'Mensagem': 'Removido com sucesso', 'Produto removido': vars(delProduto)})
    except:
        return delProduto


#  SETOR
@app.get('/setor')
def setores_get():
    setors = get_all(Setor)
    try:
        setorsJSON = jsonify([vars(setor) for setor in setors])
        return setorsJSON, 200
    except:
        return setors

@app.get('/setor/<int:id>')
def setor_get(id):
    setor = get_by_ID(Setor, id)
    try:
        if(setor):
            return jsonify(vars(setor))
        else:
            return (jsonify({'mensagem': 'Setor não encontrado'}), 404)
    except:
        return setor

@app.post('/setor')
def setor_post():
    try:
        newSetor = request.json
        newSetor = create_item(Setor, newSetor)
        return jsonify({'Mensagem': 'Novo setor criado','Novo Setor': vars(newSetor)}), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.put('/setor/<int:id>')
def setor_put(id):
    updtSetor = request.json
    setor = update_item(Setor, id, updtSetor)
    try:
        if(setor):
            return jsonify({'Mensagem': 'Setor atualizado','Setor': vars(setor)}), 201
    except:
        return setor
    
@app.delete('/setor/<int:id>')
def setor_delete(id):
    delSetor = delete_item(Setor, id)
    try:
        return jsonify({'Mensagem': 'Removido com sucesso', 'Setor removido': vars(delSetor)})
    except:
        return delSetor
    

#  USUARIO
@app.get('/usuario')
def usuarios_get():
    usuarios = get_all(Usuario)
    try:
        usuariosJSON = jsonify([vars(usuario) for usuario in usuarios])
        return usuariosJSON, 200
    except:
        return usuarios
    
@app.get('/usuario/<int:id>')
def usuario_get(id):
    usuario = get_by_ID(Usuario, id)
    try:
        if(usuario):
            return jsonify(vars(usuario))
        else:
            return (jsonify({'mensagem': 'Usuario não encontrado'}), 404)
    except:
        return usuario

@app.post('/usuario')
def usuario_post():
    try:
        newUsuario = request.json
        newUsuario = create_item(Usuario, newUsuario)
        return jsonify({'Mensagem': 'Novo usuario criado','Novo Usuário': vars(newUsuario)}), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.put('/usuario/<int:id>')
def usuario_put(id):
    updtUsuario = request.json
    usuario = update_item(Usuario, id, updtUsuario)
    try:
        if(usuario):
            return jsonify({'Mensagem': 'usuario atualizado','usuario': vars(usuario)}), 201
    except:
        return usuario
    
@app.delete('/usuario/<int:id>')
def usuario_delete(id):
    delUsuario = delete_item(Usuario, id)
    try:
        return jsonify({'Mensagem': 'Removido com sucesso', 'Usuario removido': vars(delUsuario)})
    except:
        return delUsuario