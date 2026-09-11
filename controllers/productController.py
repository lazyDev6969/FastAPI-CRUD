from fastapi import HTTPException

from models.productModel import Product

# -----------------------------
# In-memory database
# -----------------------------
products: list[Product] = []
next_id = 0


def create_product(product: Product):
    global next_id

    next_id += 1
    product.id = next_id
    products.append(product)

    return {
        "isSuccess": True,
        "message": "Product created successfully",
        "product": product,
    }


def get_products():
    return {
        "isSuccess": True,
        "products": products,
    }


def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return {
                "isSuccess": True,
                "product": product,
            }

    raise HTTPException(status_code=404, detail="Product not found")


def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            updated_product.id = product_id  # keep the existing ID
            products[index] = updated_product

            return {
                "isSuccess": True,
                "message": "Product updated successfully",
                "product": updated_product,
            }

    raise HTTPException(status_code=404, detail="Product not found")


def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted_product = products.pop(index)

            return {
                "isSuccess": True,
                "message": "Product deleted successfully",
                "product": deleted_product,
            }

    raise HTTPException(status_code=404, detail="Product not found")
