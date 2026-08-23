import requests


SHOPIFY_API_VERSION = "2021-01"  # outdated version


def get_products(shop_domain: str, access_token: str) -> list:
    """Fetch products from Shopify — uses deprecated API version."""
    url = f"https://{shop_domain}/admin/api/{SHOPIFY_API_VERSION}/products.json"
    headers = {"X-Shopify-Access-Token": access_token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["products"]


def create_order(shop_domain: str, access_token: str, order_data: dict) -> dict:
    """Create order — uses updated API schema."""
    url = f"https://{shop_domain}/admin/api/{SHOPIFY_API_VERSION}/orders.json"
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json",
    }
    payload = {
        "order": {
            **order_data,
            "line_items": [
                {
                    "variant_id": 12345,
                    "quantity": 1,
                    "fulfillment_service_id": 0,
                }
            ],
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["order"]