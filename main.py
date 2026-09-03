from fastapi import FastAPI

from routers.productRouter import router as product_router

app = FastAPI(title="Product API")

app.include_router(product_router)

# this is commet to do fetch in local


@app.get("/")
def read_root():
    return {"message": "backend is running and i have made changes for feature branch"}
