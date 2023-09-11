from fastapi import FastAPI
import asyncio
from pydantic import BaseModel

app = FastAPI()


class PostReqModel(BaseModel):
    req_id: str
    cadastre: str
    lat: float
    lon: float


class PostRespModel(BaseModel):
    req_id: str
    cadastre: str
    lat: float
    lon: float
    calc: bool


@app.post("/calculate/")
async def calculate(req: PostReqModel):
    await asyncio.sleep(10)

    response = PostRespModel(
        req_id=req.req_id,
        cadastre=req.cadastre,
        lat=req.lat,
        lon=req.lon,
        calc=True
    )

    return response
