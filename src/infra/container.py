import boto3
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Container, Resource

from infra.rdb.container import RelationalDatabaseContainer


class InfraContainer(DeclarativeContainer):
    config = Configuration()
    rdb = Container(RelationalDatabaseContainer, config=config.rdb)
    boto3_session = Resource(boto3.session.Session)
