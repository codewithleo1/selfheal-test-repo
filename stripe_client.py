import httpx


def create_payment_intent(amount: int, currency: str) -> dict:
    response = httpx.post(
        'https://api.stripe.com/v1/payment_intents',
        headers={'Authorization': 'Bearer sk_test_placeholder'},
        data={
            'amount': amount * 100,  # Stripe requires amount to be in cents
            'currency': currency,
            'payment_method_types': ['card'],
            'payment_method': 'pm_card_visa',  # example payment method
        },
    )
    return response.json()