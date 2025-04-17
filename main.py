from utils import convert_image_url_to_base64
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import Tuple, Optional

app = FastAPI(title="IMAGE CONVERTER")


@app.get("/")
def health_check():
    return "The Health Check is successful yay!!!"

# Request model


class RequestState(BaseModel):
    image_url: str
    max_size: Optional[Tuple[int, int]] = (300, 300)
    image_format: Optional[str] = 'JPEG'
    quality: Optional[int] = 50

# Convert image from URL to base64



@app.post("/image")
async def image_converter(request: RequestState):
    try:
        return {
            "base64_image": convert_image_url_to_base64(
                image_url=request.image_url,
                max_size=request.max_size,
                image_format=request.image_format,
                quality=request.quality
            )
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


