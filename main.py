from fastapi import FastAPI, UploadFile
from pyzbar import pyzbar

from utils import decode_QR, get_image

app = FastAPI()


@app.post('/decode_QR/')
async def decode_QR_route(file: UploadFile):
    image = get_image(await file.read())
    return {'decoded_data': decode_QR(image)}


@app.post('/decode_bar/')
async def decode_zbar_route(file: UploadFile):
    image = get_image(await file.read())
    return {'decoded_data': pyzbar.decode(image)[0][0]}
