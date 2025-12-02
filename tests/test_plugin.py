from __future__ import annotations

from pytest import Pytester


def test_autofocus_filters_to_marked_tests(pytester: Pytester) -> None:
    pytester.makepyfile("""
        import pytest
        def test_a(): pass
        @pytest.mark.focus
        def test_b(): pass
        def test_c(): pass
    """)
    result = pytester.runpytest("--auto-focus")
    result.assert_outcomes(passed=1)


def test_autofocus_runs_all_when_none_marked(pytester: Pytester) -> None:
    pytester.makepyfile("""
        def test_a(): pass
        def test_b(): pass
    """)
    result = pytester.runpytest("--auto-focus")
    result.assert_outcomes(passed=2)


def test_autofocus_disabled_runs_all(pytester: Pytester) -> None:
    pytester.makepyfile("""
        import pytest
        def test_a(): pass
        @pytest.mark.focus
        def test_b(): pass
    """)
    result = pytester.runpytest()
    result.assert_outcomes(passed=2)


def test_autofocus_multiple_focused(pytester: Pytester) -> None:
    pytester.makepyfile("""
        import pytest
        @pytest.mark.focus
        def test_a(): pass
        def test_b(): pass
        @pytest.mark.focus
        def test_c(): pass
    """)
    result = pytester.runpytest("--auto-focus")
    result.assert_outcomes(passed=2)
