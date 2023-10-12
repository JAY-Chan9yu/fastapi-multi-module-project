import asyncio

import pytest
from _pytest.fixtures import FixtureLookupError


@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def container():
    from container import MainContainer

    return MainContainer()


@pytest.fixture(autouse=True)
def inject_components(container, request) -> None:
    item = request._pyfuncitem  # noqa
    fixture_names = getattr(item, "fixturenames", request.fixturenames)
    for arg_name in fixture_names:
        try:
            request.getfixturevalue(arg_name)
        except FixtureLookupError as e:
            if arg_name == "inject_components":
                continue
            provided = container
            for seg in arg_name.split("__"):
                try:
                    provided = getattr(provided, seg)()
                except AttributeError:
                    raise e
            item.funcargs[arg_name] = provided
