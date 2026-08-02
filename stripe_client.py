import stripe


def create_payment_intent(amount: int, currency: str) -> dict:
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method="pm_card_visa",
    )
    return {"id": payment_intent.id, "status": payment_intent.status}