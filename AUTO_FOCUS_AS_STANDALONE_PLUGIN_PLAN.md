# pytest-autofocus: Standalone Plugin Plan

## Overview

Transition from builtin pytest plugin → independent PyPI package that users opt-in to install.

## Repository Setup

**Yes, create a new repository:** `pytest-autofocus`

Suggested location: `/Users/matt/code/pytest-autofocus`

## Package Structure

```
pytest-autofocus/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── pytest_autofocus/
│       ├── __init__.py
│       └── plugin.py
└── tests/
    └── test_plugin.py
```

## Implementation Steps

### 1. Create New Repository

```bash
cd ~/code
mkdir pytest-autofocus
cd pytest-autofocus
git init
```

### 2. Create `pyproject.toml`

Key requirements:
- Use `hatchling` as build backend
- Set `requires-python = ">=3.10"`
- Add `pytest>=7.0.0` as dependency
- Include `"Framework :: Pytest"` classifier for discoverability
- **Critical**: Define entry point under `[project.entry-points.pytest11]`
  - Name it `autofocus`
  - Point to `pytest_autofocus.plugin`

### 3. Create `src/pytest_autofocus/__init__.py`

Simple module with `__version__ = "0.1.0"`

### 4. Create `src/pytest_autofocus/plugin.py`

**Copy from**: `/Users/matt/code/pytest/src/_pytest/autofocus.py`

No changes needed - the hooks work identically in external plugins.

### 5. Create `tests/test_plugin.py`

**Copy from**: `/Users/matt/code/pytest/testing/test_autofocus.py`

Minor changes:
- Import from `pytest` not `_pytest.pytester`
- Remove `# mypy: allow-untyped-defs` if not using mypy

### 6. Create `README.md`

Include:
- Installation: `pip install pytest-autofocus`
- Basic usage example with `@pytest.mark.focus`
- Show both `--auto-focus` and normal `pytest` behavior
- pytest-watch integration: `ptw . -- --auto-focus`
- Requirements (Python 3.10+, pytest 7.0+)

### 7. Create `LICENSE`

Use MIT License (matches pytest itself)

## Testing Before Publishing

### Local Development Testing

#### 1. Test Plugin Itself

```bash
cd pytest-autofocus
uv sync
uv run pytest tests/
```

#### 2. Install Plugin in Your Existing Project

Install the plugin in editable mode from the local directory:

```bash
cd /path/to/your/existing/project
pip install -e /Users/matt/code/pytest-autofocus
```

Or if using `uv`:

```bash
cd /path/to/your/existing/project
uv pip install -e /Users/matt/code/pytest-autofocus
```

**No additional configuration needed** - pytest will auto-discover the plugin via the entry point defined in `pyproject.toml`.

#### 3. Verify Installation

Check that the plugin is registered:

```bash
pytest --help | grep auto-focus
```

Should show:
```
  --auto-focus          Only run tests marked with @pytest.mark.focus, if any
                        exist, otherwise run all.
```

#### 4. Test in Your Project

Mark some tests with `@pytest.mark.focus`:

```python
import pytest

def test_normal():
    pass

@pytest.mark.focus
def test_focused():
    pass
```

Run with auto-focus enabled:

```bash
pytest --auto-focus -v  # Should run only focused tests
pytest -v              # Should run all tests
```

If no tests are marked with `@pytest.mark.focus`, `pytest --auto-focus` will run all tests normally.

## Publishing to PyPI

### 1. Build Package

```bash
pip install build twine
python -m build
```

Creates `dist/` with `.whl` and `.tar.gz`

### 2. Test on TestPyPI (Optional but Recommended)

```bash
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ pytest-autofocus
```

### 3. Publish to PyPI

```bash
twine upload dist/*
```

Requirements:
- PyPI account
- API token from https://pypi.org/manage/account/token/
- Configure in `~/.pypirc`

## End-to-End Testing (After Publishing)

### Test Fresh Installation

```bash
cd /tmp
mkdir test-install-autofocus && cd test-install-autofocus
python3.12 -m venv venv
source venv/bin/activate
pip install pytest pytest-autofocus

# Verify registration
pytest --version
pytest --help | grep auto-focus

# Create test file with @pytest.mark.focus
# Run: pytest --auto-focus -v  → only focused tests
# Run: pytest -v              → all tests
```

### Test with pytest-watch

```bash
pip install pytest-watch
ptw . -- --auto-focus
# Edit files to add/remove @pytest.mark.focus
# Verify tests auto-filter
```

## Cleanup in pytest Repository

After publishing successfully:

```bash
cd /Users/matt/code/pytest

# Remove builtin plugin files
rm src/_pytest/autofocus.py
rm testing/test_autofocus.py

# Revert config changes
# Edit src/_pytest/config/__init__.py
# Remove "autofocus" from default_plugins tuple
```

## Important Guidelines

### Entry Point Configuration
The `[project.entry-points.pytest11]` section is what makes pytest auto-discover your plugin. The key (left side) is arbitrary, but convention is to match your plugin name. The value (right side) must point to the actual module containing your hooks.

### Naming Conventions
- Package name: `pytest-autofocus` (hyphen, as seen on PyPI)
- Import name: `pytest_autofocus` (underscore, as used in Python)
- Entry point: can be either, but underscore is cleaner

### Version Strategy
- Start with `0.1.0` for initial release
- Follow semver: `MAJOR.MINOR.PATCH`
- Bump MINOR for new features
- Bump PATCH for bug fixes
- Stay on 0.x.y until API is stable

### Testing Strategy
Always test in this order:
1. Local editable install (`pip install -e .`)
2. Fresh venv with wheel install
3. TestPyPI (staging)
4. Real PyPI
5. Clean environment with real PyPI install

## Distribution Strategy

1. **GitHub**: Push to public repository first
2. **PyPI**: Publish as `pytest-autofocus`
3. **Documentation**: README is your primary docs
4. **Changelog**: Consider CHANGELOG.md for version history
5. **Optional**: Submit to pytest-dev organization later if it gains traction

## Advantages of Standalone Plugin

✅ Users opt-in by installing  
✅ Independent versioning and releases  
✅ No pytest core changes needed  
✅ Auto-discovered by pytest via entry points  
✅ Can iterate rapidly without pytest release cycle  
✅ Discoverable on PyPI alongside 1700+ other pytest plugins  
✅ Can be disabled with `-p no:autofocus` if needed
