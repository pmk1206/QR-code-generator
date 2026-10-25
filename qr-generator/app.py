from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import qrcode
from io import BytesIO
import base64

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/generate")
def generate_qr(payload: dict):
    text = (payload.get("text",'manisha and n') or "").strip()
    if not text:
        return {"error": "Enter a link or text"}

    qr = qrcode.make(text)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    image_b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
    return {"image": "data:image/png;base64," + image_b64}
