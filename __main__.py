from http.client import BAD_REQUEST , OK
from fastapi import FastAPI, Request, Response, Query

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
async def main(
    response: Response,
    count:int  = Query()
    ):
    arr:list[int] = []
    if count <= 0:
        response.status_code = BAD_REQUEST
        return {"array":[]}
    for i in range(0,count):
        arr.append(i)

    response.status_code = OK
    return {"array":list}