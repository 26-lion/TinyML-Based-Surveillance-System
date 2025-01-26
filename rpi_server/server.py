import socket
from PIL import Image 
import io
import mesaage
from ultralytics import YOLO

img_path = "output.jpg"
address = "192.168.178.51"
port = 21042
server = socket.socket()
server.bind((address,port))
model_path = "best_float16.tflite"
server.listen(1)
model = YOLO(model_path)


def create_image_from_bytes(image_bytes):
    stream = io.BytesIO(image_bytes)
    return Image.open(stream)

while True:
    c,address_client = server.accept()
    array_from_client = bytearray()
    while True:
        data = c.recv(1024)
        if not data:
            break
        else:
            array_from_client.extend(data)
    img = create_image_from_bytes(array_from_client)
    results = model(img,task="detect")
    results[0].save()
    if results[0].boxes.conf.nelement()!=0:
        mesaage.send_message
    c.close()
