import stripe


def create_payment_intent(amount: int, currency: str) -> dict:
    """Create a Stripe payment intent."""
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method_data={
            "type": "card",
            "card": {
                "number": "4242424242424242",
                "exp_month": 12,
                "exp_year": 2025,
                "cvc": "123",
            },
        },
        confirm=True
    )
    return {"id": payment_intent.id, "status": payment_intent.status}