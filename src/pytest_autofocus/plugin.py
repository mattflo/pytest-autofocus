"""Auto-focus plugin: run only @pytest.mark.focus tests when --auto-focus is set."""

from __future__ import annotations

from pytest import Config
from pytest import Item
from pytest import Parser


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("general")
    group.addoption(
        "--auto-focus",
        action="store_true",
        default=False,
        help="Only run tests marked with @pytest.mark.focus, if any exist, otherwise run all.",
    )


def pytest_configure(config: Config) -> None:
    config.addinivalue_line("markers", "focus: mark test to run in auto-focus mode")


def pytest_collection_modifyitems(items: list[Item], config: Config) -> None:
    if not config.getoption("auto_focus"):
        return

    focused = [item for item in items if item.get_closest_marker("focus")]
    if not focused:
        return

    deselected = [item for item in items if item not in focused]
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = focused
