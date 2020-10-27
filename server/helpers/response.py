from flask import jsonify

def success(msg, data):
  return jsonify({ 'error': False, 'msg': msg, 'data': data })

def error(err_code, msg):
  return jsonify({ 'error': True, 'error_code': err_code, 'msg': msg })


