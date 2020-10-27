import sys
sys.path.insert(0, "./helpers/")

from flask import Flask, jsonify, request
from flask_cors import CORS
import pyqrcode
from time import time
from helpers import response

# configuration
DEBUG = True


# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)
# set environment
app.testing = True

# enable CORS
CORS(app, resources={ r'/*': { 'origins': '*' } })

@app.route('/', methods=['GET'])
def home():
  return response.success('Welcome to VueQR', request.host_url)

@app.route('/generate', methods=['POST', 'GET'])
def generate():
  """
     @api {POST} /generate Generate QRCode
     @apiName generate
     @apiGroup QRCode
     @apiVersion  1.0.0


     @apiParam  {String} url website url to generate from
     @apiParam  {String} bgColor background color for QRcode image in HEX

     @apiSuccess (200) {Object} success success response

     @apiParamExample  {Object} Request-Example:
     {
         url : 'www.facebook.com',
         bgColor : '#FFFFFF',
         codeColor: '#000000'
     }


     @apiSuccessExample {Object} Success-Response:
     {
         error : False,
         msg: 'QRcode generated!',
         url: 'www.sososos.com/image.png'
     }
  """
  if request.method == 'POST':
    request_payload = request.get_json()
    website_url = request_payload.get('url')
    bg_color = request_payload.get('bgColor') or '#FFFFFF'
    code_color = request_payload.get('codeColor') or '#000000'

    if not website_url:
      return response.error(422, 'provide a website url')

    img = pyqrcode.create(website_url)
    filename = time()
    hostname = request.host_url
    file_path = f'static/{filename}.png'

    img.png(file_path, scale= 10, module_color=code_color, background=bg_color)

    return response.success('QRcode generated!', { 'url': f'{hostname}{file_path}' })
  else:
    return response.error(400, 'this route supports POST actions')


if __name__ == "__main__":
  app.run()
