from typing import List

from fastapi_crudrouter import OrmarCRUDRouter

from . import models, schemas

# POST

post_router = OrmarCRUDRouter(
    schema=models.Post,
    create_schema=schemas.PostBase,
)


@post_router.get('', response_model=List[schemas.PostOut])
async def get_all():
    return await models.Post.objects.all()


# CATEGORY

category_router = OrmarCRUDRouter(
    schema=models.Category,
    create_schema=schemas.CategoryBase,
    delete_all_route=False,
)


@category_router.get('', response_model=List[schemas.CategoryOut])
async def get_all():
    return await models.Category.objects.all()


# COMMENT

comment_router = OrmarCRUDRouter(
    schema=models.Comment,
    create_schema=schemas.CommentBase,
)
