import base64

def img_to_base64(image_path: str):
  """
    this function generates base64 string from a provided image
  """
  with open(image_path, 'rb') as img_file:
    encoded_string = base64.b64encode(img_file.read())

    return encoded_string.decode('utf-8')

