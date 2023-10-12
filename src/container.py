from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Container

from domains.container import DomainsContainer
from infra.container import InfraContainer
from systems.container import SystemContainer


class MainContainer(DeclarativeContainer):
    # Configurations
    config = Configuration(yaml_files=["config.yml"])
    wiring_config = WiringConfiguration(packages=["applications"])

    # Infra
    infra = Container(InfraContainer, config=config.infra)

    # Systems
    systems = Container(SystemContainer, config=config.systems)

    # Domains
    domains = Container(
        DomainsContainer,
        config=config.domains,
        user_repository=infra.rdb.users.user_repository,
        notification_push_api=systems.notification_push_api,
    )
