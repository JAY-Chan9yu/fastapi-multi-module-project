from typing import Any


class NotificationPushAPI:
    def __init__(self, base_url: str, secret_key: str):
        self.base_url = base_url
        self.secret_key = secret_key

    async def enqueue_push(self, message_id: str, payload: dict[str, Any]) -> None:
        # Implement this method!
        print(f"push message enqueued: {message_id}, {payload}")
        pass
