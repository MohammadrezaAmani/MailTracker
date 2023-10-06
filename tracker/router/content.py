from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from uuid import uuid4
from tracker.models.content import ContentDB, ViewDB
from tracker._config import DATABASE
import datetime
import pathlib

BASE_PATH = pathlib.Path(__file__).parent.parent.parent
router = APIRouter(
    prefix="/content",
    tags=["Content"],
)


@router.get("")
async def get_links():
    return jsonable_encoder(DATABASE.get_contents())


@router.post("/add")
async def add_content():
    id = str(uuid4())
    content = ContentDB(
        id=id,
        assets="/tracker/assets/media/defult.png",
        link=id,
        created_at=datetime.datetime.now(),
        user=1,
        views=[],
    )
    if DATABASE.add_content(content):
        return JSONResponse(
            status_code=201, content={"message": "Content added successfully"}
        )
    return JSONResponse(status_code=400, content={"message": "Content not added"})


@router.get("/{id}")
async def get_content(id, request: Request):
    view = ViewDB(
        id=str(uuid4()),
        countery=request.client.host,
        ip=request.client.host,
        created_at=datetime.datetime.now(),
        request=(request.headers.__dict__),
    )
    DATABASE.add_view_to_content(id, view)
    return FileResponse(
        str(BASE_PATH) + DATABASE.search_content(id).assets, media_type="image/png"
    )


@router.get("/{id}/views")
async def get_views(id):
    return jsonable_encoder(DATABASE.search_content(id).views)
