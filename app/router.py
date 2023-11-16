from fastapi import APIRouter

from .service import define_a_template

router_template = APIRouter()


@router_template.post('/')
async def get_template(data: dict):
    return await define_a_template(data)
