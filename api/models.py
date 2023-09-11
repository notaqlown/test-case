from pydantic import BaseModel


class PostRequestModel(BaseModel):
    cadastre: str
    lat: float
    lon: float


class PostResponseModel(BaseModel):
    req_id: str


class GetResponseModel(BaseModel):
    req_id: str
    cadastre: str
    lat: float
    lon: float


