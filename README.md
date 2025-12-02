# pytest-autofocus

Auto-focus plugin for pytest: run only `@pytest.mark.focus` tests when `--auto-focus` is set, otherwise run all tests.

## Installation

```bash
pip install pytest-autofocus
```

## Usage

Mark tests with `@pytest.mark.focus`:

```python
import pytest

def test_normal():
    pass

@pytest.mark.focus
def test_focused():
    pass
```

Run with `--auto-focus` to run only focused tests (if any exist), otherwise run all tests:

```bash
pytest --auto-focus
```

If no tests are marked with `@pytest.mark.focus`, all tests run normally.

Run without `--auto-focus` to run all tests:

```bash
pytest
```

## pytest-watcher Integration

Use with [pytest-watcher](https://github.com/olzhasar/pytest-watcher) for automatic test filtering:

```bash
ptw . -- --auto-focus
```

## Requirements

- Python 3.10+
- pytest 7.0+

