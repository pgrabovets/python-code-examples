import base64
from sys import argv

if len(argv) == 2:
    image_path = argv[1]
    image_file = open(image_path, 'rb')
    image_b = base64.b64encode(image_file.read())
    print(image_b.decode('utf-8'))
else: 
    print('Type image path')
