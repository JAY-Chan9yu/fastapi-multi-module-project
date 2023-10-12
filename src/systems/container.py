from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .notification_push_api.client import NotificationPushAPI


class SystemContainer(DeclarativeContainer):
    config = Configuration()
    notification_push_api = Factory(
        NotificationPushAPI,
        base_url=config.notification_push_api.base_url,
        secret_key=config.notification_push_api.secret_key,
    )
