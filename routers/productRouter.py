from fastapi import APIRouter

from models.productModel import Product
from controllers import productController

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("", status_code=201)
def create_product(product: Product):
    return productController.create_product(product)


@router.get("")
def get_products():
    return productController.get_products()


@router.get("/{product_id}")
def get_product(product_id: int):
    return productController.get_product(product_id)


@router.put("/{product_id}")
def update_product(product_id: int, updated_product: Product):
    return productController.update_product(product_id, updated_product)


@router.delete("/{product_id}")
def delete_product(product_id: int):
    return productController.delete_product(product_id)
