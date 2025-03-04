from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import qrcode

app = FastAPI()

@app.post("/generate_qr")
def generate_qr(text: str = Form(...)):
    qr = qrcode.make(text)
    qr_path = "qrcode.png"
    qr.save(qr_path)
    return FileResponse(qr_path, media_type="image/png", filename="qrcode.png")
