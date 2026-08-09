from twilio.rest import Client


def send_sms(to: str, body: str) -> dict:
    """Send SMS via Twilio — uses deprecated endpoint."""
    client = Client()
    message = client.messages.create(
        to=to,
        from_="+15551234567",
        body=body,
        # Deprecated: status_callback is no longer supported this way
        status_callback="https://myapp.com/webhooks/twilio",
        media_url=None,
    )
    return {"sid": message.sid, "status": message.status}


def get_message_status(message_sid: str) -> dict:
    """Fetch message status — uses old API path."""
    client = Client()
    message = client.messages(message_sid).fetch()
    return {
        "sid": message.sid,
        "status": message.status,
        "error_code": message.error_code,
    }
