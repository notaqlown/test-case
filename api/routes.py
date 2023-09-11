from fastapi import BackgroundTasks
import requests
import asyncio
from main import app, channel, connection
import uuid
from database import Session, Request
from models import GetResponseModel, PostResponseModel, PostRequestModel
import json
import logging
import sys

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])


@app.post("/generate-id", response_model=PostResponseModel)
async def generate_id(request: PostRequestModel):
    req_id = str(uuid.uuid4())
    data = {
        'req_id': req_id,
        'cadastre': request.cadastre,
        'lat': request.lat,
        'lon': request.lon,
    }
    channel.basic_publish(exchange='', routing_key='dummy-queue', body=json.dumps(data))
    response = PostResponseModel(req_id=req_id)
    return response


@app.get('/get-by-id/{req_id}')
async def get_info(req_id: str):
    session = Session()
    data = session.query(Request).filter(Request.id == req_id).first()
    if data:
        response = GetResponseModel(req_id=data.id,
                                    cadastre=data.cadastre,
                                    lat=data.latitude,
                                    lon=data.longitude)
        return response
    else:
        return {"error": "Request not found"}


@app.on_event("shutdown")
async def shtdwn():
    connection.close()
