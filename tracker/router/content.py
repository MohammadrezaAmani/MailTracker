from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder
from uuid import uuid4
from tracker.models.content import ContentAdd, ContentDB, ViewDB
from tracker._config import DATABASE
import datetime

router = APIRouter(
    prefix="/content",
    tags=["Content"],
)


@router.get("")
async def get_links():
    return jsonable_encoder(DATABASE.get_contents())


@router.post("")
async def add_content(content: ContentAdd):
    content = ContentDB(
        id=str(uuid4()),
        assets=content.assets,
        link=content.link,
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
    return jsonable_encoder(view)


@router.get("/{id:int}/views")
async def get_views(id: int):
    return jsonable_encoder(DATABASE.search_content(id).views)
