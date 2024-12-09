import sqlite3
from flask import jsonify
from helpers.database import getConnection

def get_all(model):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM tb_{model.__name__}")
        resultset = cursor.fetchall()
        return [model(*item) for item in resultset]
    
    except sqlite3.Error as e:
        return jsonify({'Error': str(e)}), 500
    
def get_by_ID(model, id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = f"SELECT * FROM tb_{model.__name__} WHERE id = ?"
        cursor.execute(query, (id, ))
        resultset = cursor.fetchone()
        if(resultset):
            return model(*resultset)
        else:
            return
    except sqlite3.Error as e:
        return jsonify({'Error': str(e)}), 500

def create_item(model, newItem):
    conn = getConnection()
    cursor = conn.cursor()
    columns = ', '.join(newItem.keys())
    values = ', '.join(['?'] * len(newItem))
    query = f'INSERT INTO tb_{model.__name__} ({columns}) VALUES ({values})'

    cursor.execute(query, tuple(newItem.values()))
    conn.commit()

    newItem['id'] = cursor.lastrowid
    return model(**newItem)
    
def update_item(model, id, novoItem):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        setItens = ', '.join([f"{key} = ?" for key in novoItem.keys()])
        query = f"UPDATE tb_{model.__name__} SET {setItens} WHERE id = ?"
        params = tuple(novoItem.values()) + (id, )
        cursor.execute(query, params)
        conn.commit()
        if cursor.rowcount > 0:
            updated_item = get_by_ID(model, id)
            return updated_item
        
    except sqlite3.Error as e:
        return jsonify({'Error': str(e)}), 500
    
    return jsonify({'Mensagem': f'{model.__name__} não encontrado(a) ou não houve alterações'}), 404

def delete_item(model, id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        resultset = get_by_ID(model, id)
        if(resultset):
            query = f'DELETE FROM tb_{model.__name__} WHERE id=?'
            cursor.execute(query, (id, ))
            conn.commit()
            return resultset
        
    except sqlite3.Error as e:
        return jsonify({'Error': str(e)}), 500
    
    return jsonify({'Mensagem': f'{model.__name__} não encontrado(a) ou não houve alterações'}), 404