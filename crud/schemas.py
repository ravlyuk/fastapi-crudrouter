from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryOut(CategoryBase):
    id: int


class PostBase(BaseModel):
    title: str
    text: str
    category: int = 1
    draft: bool = False

    class Config:
        orm_mode = True


class PostOut(PostBase):
    id: int
    category: CategoryOut


class CommentBase(BaseModel):
    text: str
    post: int


class CommentOut(BaseModel):
    id: int
    post: PostOut
