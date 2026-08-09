import stripe


def create_payment_intent(amount: int, currency: str) -> dict:
    """Create a Stripe payment intent."""
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method_types=["card"],
        setup_future_usage="off_session",
    )
    return {"id": payment_intent.id, "status": payment_intent.status}