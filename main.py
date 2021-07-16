from fastapi import FastAPI
import uvicorn
from db import database, metadata, engine
from crud.api import post_router, comment_router, category_router

app = FastAPI()
app.state.database = database

metadata.create_all(engine)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(post_router)
app.include_router(comment_router)
app.include_router(category_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True, debug=True)
