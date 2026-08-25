import httpx


def create_payment_intent(amount: int, currency: str) -> dict:
    response = httpx.post(
        'https://api.stripe.com/v1/payment_intents',
        headers={'Authorization': 'Bearer sk_test_placeholder'},
        json={
            'amount': amount * 100,
            'currency': currency,
            'payment_method_types': ['card'],
        },
    )
    return response.json()